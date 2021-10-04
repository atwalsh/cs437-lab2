from flask import Blueprint

controls_bp = Blueprint('controls_bp', __name__, url_prefix='/controls')


@controls_bp.route('/forward')
def forward():
    return 'forward'


@controls_bp.route('/back')
def back():
    return 'back'


@controls_bp.route('/left')
def left():
    return 'left'


@controls_bp.route('/right')
def right():
    return 'right'
