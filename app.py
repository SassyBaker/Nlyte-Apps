from flask import Flask, render_template
from apps.qr_code_generator import qr_code_generator_bp

app = Flask(__name__)

SITE_TITLE = "Nlyte Companion Apps"

# Register blueprints
app.register_blueprint(qr_code_generator_bp, url_prefix="/apps/qr_code_generator")

@app.route("/")
def index():
    return render_template('index.html', site_title=SITE_TITLE)

if __name__ == "__main__":
    app.run(debug=True)
