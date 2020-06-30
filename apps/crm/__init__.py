from flask import Blueprint

crm_api = Blueprint('crm_api', __name__, url_prefix="/api/v1")

from apps.crm import goods_list_view
