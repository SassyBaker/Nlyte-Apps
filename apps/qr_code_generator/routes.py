from flask import render_template
import random
from . import qr_code_generator_bp


def generate_code():
    """Generate a unique 7-digit code prefixed with 'NeedsQR-'."""
    code = f"NeedsQR-{random.randint(1000000, 9999999)}"
    return code


@qr_code_generator_bp.route("/")
def index():
    code = generate_code()
    return render_template("qr_code_generator/index.html", code=code)

@qr_code_generator_bp.route("/generate", methods=["POST"])
def generate():
    code = generate_code()
    return render_template("qr_code_generator/_code_snippet.html", code=code)
