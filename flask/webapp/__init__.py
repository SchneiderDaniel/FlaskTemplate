import sys
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from webapp.config import Config
from flask_migrate import Migrate
from flask import request

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class=Config):
    print('Start creating the app',  file=sys.stderr)
    app = Flask(__name__)
    print('Start configure the app',  file=sys.stderr)

    app.config.from_object(Config)

    from webapp.main.routes import main
    from webapp.errors.handlers import errors
    

    app.register_blueprint(main)
    app.register_blueprint(errors)
    
    db.init_app(app)
    migrate.init_app(app,db)
  

    print('Done creating the app',  file=sys.stderr)
    return app



