from io import BytesIO
from flask import Blueprint, Response
import io
from threading import Condition
import time

from picamera import PiCamera

camera_bp = Blueprint('camera_bp', __name__, url_prefix="/camera")

# taken from https://picamera.readthedocs.io/en/release-1.13/recipes2.html#web-streaming
class StreamingOutput(object):
    def __init__(self):
        self.frame = None
        self.buffer = io.BytesIO()
        self.condition = Condition()

    def write(self, buf):
        if buf.startswith(b'\xff\xd8'):
            # New frame, copy the existing buffer's content and notify all
            # clients it's available
            self.buffer.truncate()
            with self.condition:
                self.frame = self.buffer.getvalue()
                self.condition.notify_all()
            self.buffer.seek(0)
        return self.buffer.write(buf)

def feed():
    output = StreamingOutput()
    with PiCamera(resolution="640x480") as cam:
        try:
            cam.start_recording(output, format="mjpeg")
            time.sleep(1)
            while True:
                frame = output.frame
                if frame:
                    yield (b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        finally:
            cam.stop_recording()

@camera_bp.route("/video")
def video():
    return Response(feed(), mimetype="multipart/x-mixed-replace; boundary=frame")
