from apps.crm import crm_api
from flask import current_app as app


@crm_api.route("/index/", methods=["GET"])
def crm_index():
    app.logger.info("this is index")
    return "ok"
