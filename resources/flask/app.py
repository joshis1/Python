from flask import Flask, jsonify, request

# initialize our flask application

app = Flask(__name__)

@app.route("/api/v1/bluetooth/settings", methods=["GET"])
def get_bluetooth_settings():
    """
    Get bluetooth status
    """
    val = {
            "enabled": True,
            "displayName": "Test"
        }

    return val


if __name__ == "__main__":
    app.run(debug=True)
