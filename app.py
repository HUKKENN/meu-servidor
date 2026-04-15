from flask import Flask, request, jsonify

app = Flask(__name__)

dados = {"Eu amo a mãe do hodnilson": 0.0}

@app.route("/set", methods=["POST"])
def set_valor():
    global dados
    dados["valor"] = float(request.json["valor"])
    return "OK"

@app.route("/get", methods=["GET"])
def get_valor():
    return jsonify(dados)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
