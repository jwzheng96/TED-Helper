from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from sqlalchemy.ext.declarative import declarative_base
import os
from config import Config
from app import app, db

os.environ["db_uri"] = Config.SQLALCHEMY_DATABASE_URI  # coin-token-lib config
migrate = Migrate()
if db.engine.url.drivername == 'sqlite':
    migrate.init_app(app, db, render_as_batch=True)
else:
    migrate.init_app(app, db)
manager = Manager(app)

from models.ted import TED

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
