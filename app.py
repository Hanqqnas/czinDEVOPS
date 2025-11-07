from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/hello")
def hello():
	return jsonify({"message": "Hello World"})

@app.route("/")
def index():
	return jsonify({"message": "Witaj na web serwisie! Aby przejść dalej przejdż do /hello"})

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000)
