# allow dynamic modules
from importlib import import_module

# load application vars
from application.config.database import *

# load driver
database = import_module('application.libraries.db_drivers.' + config['driver'], )

# load database
config.pop('driver', None)
db = database.Driver(**config)
