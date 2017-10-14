class Config:
    SECRET_KEY = "gcysdh7ew63q98ytbcxybgv_hygfd653267"

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    """development configurations"""

class TestingConfig(Config):
    TESTING = True
    """testing configurations"""

class ProductionConfig(Config):
    """prodution cnfigurations"""


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
