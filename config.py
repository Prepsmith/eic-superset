"""The main config file for Superset

All configuration in this file can be overridden by providing a superset_config
in your PYTHONPATH as there is a ``from superset_config import *``
at the end of this file.
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from superset.custom.eic_session import EicSupersetSecureSessionInterface

import os

from superset.stats_logger import DummyStatsLogger

# Realtime stats logger, a StatsD implementation exists
STATS_LOGGER = DummyStatsLogger()

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
BASE_DIR = os.path.join(BASE_DIR, 'superset')

if 'SUPERSET_HOME' in os.environ:
    DATA_DIR = os.environ['SUPERSET_HOME']
else:
    DATA_DIR = 'superset'
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

#---------------------------------------------------------
# Superset specific config
#---------------------------------------------------------
ROW_LIMIT = 50000
VIZ_ROW_LIMIT = 10000
SUPERSET_WORKERS = 4

SUPERSET_WEBSERVER_PORT = 4400
SUPERSET_WEBSERVER_ADDRESS = '0.0.0.0'
SUPERSET_WEBSERVER_TIMEOUT = 120
EMAIL_NOTIFICATIONS = False
#---------------------------------------------------------

#---------------------------------------------------------
# Flask App Builder configuration
#---------------------------------------------------------
# Your App secret key
SECRET_KEY = 'a5prfkLThjqdaKtUKUBmwWPHQZ6PgJZ3'

# The SQLAlchemy connection string to your database backend
# This connection defines the path to the database that stores your
# superset metadata (slices, connections, tables, dashboards, ...).
# Note that the connection information to connect to the datasources
# you want to explore are managed directly in the web UI
SQLALCHEMY_DATABASE_URI = 'postgresql://eic_admin@localhost/eic_superset_develop'

# Flask-WTF flag for CSRF
WTF_CSRF_ENABLED = True

ENABLE_TIME_ROTATE = True
TIME_ROTATE_LOG_LEVEL = 'DEBUG'
FILENAME = "/home/vagrant/incubator-superset/superset.log"
ROLLOVER = "midnight"
INTERVAL = 1
BACKUP_COUNT = 30

ADDITIONAL_MIDDLEWARE = [EicSupersetSecureSessionInterface, ]
