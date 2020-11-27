from flask import Flask, jsonify


app = Flask(__name__, static_url_path="")


@app.route("/json", methods=["GET"])
def get_json():
    first = {"id": 1, "name": "Francisco", "apellido": "Martinez"}
    second = {"id": 1, "name": "John", "apellido": "Dow"}
    data = [first, second]
    return jsonify(data)


@app.route("/", methods=["GET"])
def saludo():
    return "Hola Enrouters"


if __name__ == "__main__":
    app.run(debug=True)