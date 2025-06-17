from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    from app.routes.home import home_bp
    app.register_blueprint(home_bp)

    from app.routes.customers import customer_bp
    app.register_blueprint(customer_bp, url_prefix="/customers")

    from app.routes.dues import due_bp
    app.register_blueprint(due_bp, url_prefix="/dues")

    return app
