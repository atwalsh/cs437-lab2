from flask import Blueprint

from picar_4wd.utils import getIP

data_bp = Blueprint('data_bp', __name__, url_prefix='/data')


@data_bp.route('/ip-info')
def ip_info():
    return str(getIP())
