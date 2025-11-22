from flask import render_template
from . import qr_code_generator_bp

@qr_code_generator_bp.route("/")
def index():
    return render_template("qr_code_generator/index.html")
