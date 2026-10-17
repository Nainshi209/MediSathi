from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route("/reports")
def reports_page():
    return send_from_directory(".", "reports.html")


@app.route("/test")
def test():
    return jsonify({
        "status": "success",
        "message": "MediSathi backend is connected!"
    })


@app.route("/analyze", methods=["POST"])
def analyze():

    data = request.get_json()

    report_type = data.get("reportType", "")
    report_details = data.get("reportDetails", "")

    if not report_type or not report_details:
        return jsonify({
            "error": "Please provide report type and details."
        }), 400

    # Temporary connection test
    return jsonify({
        "status": "success",
        "message": "Report details successfully received by MediSathi backend!",
        "reportType": report_type
    })


if __name__ == "__main__":
    app.run(debug=True)