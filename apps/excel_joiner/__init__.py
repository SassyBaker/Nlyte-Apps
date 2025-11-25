from flask import Blueprint

excel_joiner_bp = Blueprint(
    "excel_joiner_bp",
    __name__,
    url_prefix="/apps/excel_joiner",
    template_folder="templates"
)


from . import routes  # imports the routes after blueprint is created
