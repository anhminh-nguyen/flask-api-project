from flask import Flask, jsonify, request

app = Flask(__name__)


# GET endpoint: Return a welcome message
@app.route("/hello", methods=["GET"])
def hello():
    return jsonify({
        "message": "Welcome to my Flask API!"
    }), 200


# GET and POST endpoint: Retrieve or submit sample data
@app.route("/data", methods=["GET", "POST"])
def data():
    if request.method == "POST":
        new_data = request.get_json(silent=True)

        if not isinstance(new_data, dict):
            return jsonify({
                "error": "A JSON object is required"
            }), 400

        return jsonify({
            "message": "Data received successfully",
            "data": new_data
        }), 201

    return jsonify({
        "students": [
            {"id": 1, "name": "Alex"},
            {"id": 2, "name": "Sarah"}
        ]
    }), 200


if __name__ == "__main__":
    app.run(debug=True)
