from flask import Blueprint

import picar_4wd as fc

controls_bp = Blueprint('controls_bp', __name__, url_prefix='/controls')

POWER_VAL = 25


@controls_bp.route('/forward')
def forward():
    fc.forward(POWER_VAL)
    return 200


@controls_bp.route('/backward')
def backward():
    fc.backward(POWER_VAL)
    return 200


@controls_bp.route('/left')
def left():
    fc.turn_left(POWER_VAL)
    return 200


@controls_bp.route('/right')
def right():
    fc.turn_right(POWER_VAL)
    return 200
