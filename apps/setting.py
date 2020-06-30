import os

BASE_DIR = os.path.dirname(__file__)


class Config:
    DEBUG = True
    BASEDIR = BASE_DIR


class DevConfig(Config):
    pass


class AlphaConfig(Config):
    pass


class ProductConfig(Config):
    pass


config = {
    "dev": DevConfig,
    "alpha": AlphaConfig,
    "prod": ProductConfig
}

# if __name__ == '__main__':
#     print(os.path.abspath(os.path.join(os.path.join(BASE_DIR, os.path.pardir), 'logs')))
#     print(BASEDIR)
#     print(os.path.join(BASEDIR, os.path.pardir))
#     print(os.path.abspath(os.path.join(os.path.dirname("__file__"), os.path.pardir)))


# C:/Users/Administrator/Desktop/python-test/flask_demo1/apps
# C:/Users/Administrator/Desktop/python-test/flask_demo1/apps\..
# C:\Users\Administrator\Desktop\python-test\flask_demo1
