from flask import Flask
from flask.helpers import send_file
from flask.templating import render_template

from blueprints.controls import controls_bp
from blueprints.data import data_bp
from blueprints.camera import camera_bp

app = Flask(__name__)
# Register blueprints
app.register_blueprint(controls_bp)
app.register_blueprint(data_bp)
app.register_blueprint(camera_bp)

@app.route("/")
def index():
    print("Rendering index")
    return send_file("static/index.html")

if __name__ == '__main__':
    # Run server
    app.run(debug=True, host='0.0.0.0')