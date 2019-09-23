import os
os.environ['PYTHON_EGG_CACHE'] = '/tmp'
import sys
sys.path.insert(0, "/var/www/waitercaller")
from waitercaller import app as application
