
import os
class Config(object):
    SECRET_KEY=os.environ.get('SECRET_KEY') or "secret-string"
    MONGODB_SETTINGS={'db':'banking'} #our database name will be Banking