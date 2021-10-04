from flask import Blueprint

from picar_4wd import Ultrasonic, Pin
from picar_4wd.utils import getIP, cpu_temperature, cpu_usage as _cpu_usage

data_bp = Blueprint('data_bp', __name__, url_prefix='/data')

us = Ultrasonic(Pin('D8'), Pin('D9'))


@data_bp.route('/ip')
def ip_info():
    """Get the Pi's IP address."""
    return str(getIP())


@data_bp.route('/distance')
def distance():
    """Get a distance reading (in cm) from the ultrasonic sensor."""
    return str(us.get_distance())


@data_bp.route('/cpu-temp')
def cpu_temp():
    """Get the Pi's CPU temp in Celsius."""
    return str(cpu_temperature())


@data_bp.route('/cpu-usage')
def cpu_usage():
    """Get the Pi's CPU usage."""
    return str(_cpu_usage())
