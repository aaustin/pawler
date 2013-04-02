# form stuff
CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

# database stuff
import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'mysql://root:pawler@localhost/pawlerdb?unix_socket=/var/run/mysqld/mysqld.sock'
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
