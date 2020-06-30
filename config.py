from decouple import config

class Config:
    #Class to create secret key
    SECRET_KEY = 'DaTa0504'

class DevelopmentConfig(Config):
    #Class to instantiate users database and parameters to send an email to each new user who registers 
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@localhost/project_web_python'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'correo@gmail.com'
    MAIL_PASSWORD = config('MAIL_PASSWORD')

class TestConfig(Config):
    #Class to instantiate tests database
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@localhost/project_web_python_test'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TEST = True

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig,
    'test': TestConfig
}    