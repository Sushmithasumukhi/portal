class Config(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    SECRET_KEY = "thisissecter"
    # SECURITY_PASSWORD_SALT = "thisissaltt"
    # SECURITY_PASSWORD_HASH="bcrypt"
    # SQLALCHEMY_TRACK_MODIFICATIONS = False
    # WTF_CSRF_ENABLED = False
    # SECURITY_TOKEN_AUTHENTICATION_HEADER = 'Authentication-Token'
    
    # ALLOWED_IMAGE_FILE = ['jpg','png','jpeg','jfif','gif']

class DevelopementConfig(Config):
    DEBUG = True