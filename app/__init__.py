# FILE: app/__init__.py
import os
from flask import Flask

def create_app():
    app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), 'templates'))

    app.config['SECRET_KEY'] = 'supersecretkey'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ces.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Import db INSIDE the function to avoid circular import errors
    from app.core.extensions import db
    db.init_app(app)

    # Register blueprints
    from app.modules.public.routes import public_bp
    from app.modules.auth.routes import auth_bp

    app.register_blueprint(public_bp)
    app.register_blueprint(auth_bp)

    return app