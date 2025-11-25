from flask import Blueprint, request, render_template, send_file
import pandas as pd
import io

# blueprint imported from __init__.py inside this package
from . import excel_joiner_bp


@excel_joiner_bp.route("/")
def index():
    return render_template("excel_joiner/index.html")


@excel_joiner_bp.route("/combine", methods=["POST"])
def combine_files():
    uploaded_files = request.files.getlist("files")

    if not uploaded_files or uploaded_files == [None]:
        return "No files uploaded"

    combined_df = pd.DataFrame()

    for file in uploaded_files:
        name = file.filename.lower()

        # Determine file type
        if name.endswith(".csv"):
            df = pd.read_csv(file)
        elif name.endswith(".xlsx") or name.endswith(".xls"):
            df = pd.read_excel(file)
        else:
            return f"Unsupported file type: {name}"

        combined_df = pd.concat([combined_df, df], ignore_index=True)

    # Output file in memory
    output = io.BytesIO()
    combined_df.to_excel(output, index=False, sheet_name="Combined")
    output.seek(0)

    return send_file(
        output,
        download_name="combined.xlsx",
        as_attachment=True,
        mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )
