from flask import Flask, render_template, jsonify
from apps.qr_code_generator import qr_code_generator_bp

app = Flask(__name__)

SITE_TITLE = "Nlyte Companion Apps"

# Register blueprints
app.register_blueprint(qr_code_generator_bp, url_prefix="/apps/qr_code_generator")

@app.route("/")
def index():
    return render_template('index.html', site_title=SITE_TITLE)

@app.route("/health")
def health_check():
    return jsonify({"status": "ok"}), 200


if __name__ == "__main__":
    app.run(debug=True)
