from flask import Blueprint

qr_code_generator_bp = Blueprint(
    "qr_code_generator_bp",
    __name__,
    template_folder="templates"
)

# Import routes AFTER the blueprint is defined
from . import routes
