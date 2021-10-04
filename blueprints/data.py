from flask import Blueprint

from picar_4wd import Ultrasonic, Pin
from picar_4wd.utils import getIP

data_bp = Blueprint('data_bp', __name__, url_prefix='/data')

us = Ultrasonic(Pin('D8'), Pin('D9'))


@data_bp.route('/ip')
def ip_info():
    return str(getIP())


@data_bp.route('/distance')
def distance():
    return str(us.get_distance())
