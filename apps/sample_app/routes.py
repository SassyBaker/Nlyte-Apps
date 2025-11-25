from flask import render_template, request
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

@qr_code_generator_bp.route("/generate-batch", methods=["POST"])
def generate_batch():
    try:
        count = int(request.form.get("count", 10))
        count = max(1, min(count, 500))  # Safety clamp: 1–500
    except ValueError:
        count = 10

    codes = [generate_code() for _ in range(count)]
    return render_template("qr_code_generator/_code_table.html", codes=codes)