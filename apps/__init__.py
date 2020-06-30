from flask import Flask
from apps.setting import config
from apps.tools.log_conf import created_handler


def register_crm_bp(app: Flask):
    from apps.crm import crm_api
    app.register_blueprint(crm_api)


def created_app(config_name="dev"):
    app = Flask(__name__)
    try:
        conf = config[config_name]
    except:
        raise IndexError("config is error!!!")

    # 导入配置文件
    app.config.from_object(conf)
    register_crm_bp(app)

    # 配置日志
    app.logger.addHandler(created_handler(conf.BASEDIR))
    return app
