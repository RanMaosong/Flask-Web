import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:147258@localhost:3306/flask?charset=utf8'
    MAIL_SERVER = 'smtp.163.com'
    MAIL_PORT = 25
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'rmslangying@163.com'
    MAIL_PASSWORD = 'rms147258'
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = 'rmslangying@163.com'
    
    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    pass


class TestingCOnfig(Config):
    pass


class ProductionConfig(Config):
    pass


config = {
    'development': DevelopmentConfig,
    'testing': TestingCOnfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}