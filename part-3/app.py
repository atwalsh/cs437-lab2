from flask import Flask

from blueprints.controls import controls_bp
from blueprints.data import data_bp

if __name__ == '__main__':
    app = Flask(__name__)

    # Register blueprints
    app.register_blueprint(controls_bp)
    app.register_blueprint(data_bp)

    # Run server
    app.run(debug=True, host='0.0.0.0')
