import os
import mysql.connector
from flask import Flask, jsonify

app = Flask(__name__)


def get_db_connection():
	return mysql.connector.connect(
		host = os.environ.get("DB_HOST", "mysql-db"),
		port = int(os.environ.get("DB_PORT", "3306")),
		user = os.environ.get("DB_USER", "appuser"),
		password = os.environ.get("DB_PASSWORD", "apppassword"),
		database = os.environ.get("DB_NAME", "mydb")
	)

@app.route("/")
def index():
	return jsonify({
		"message": "Witaj na web serwisie!",
		"endpoints": ["/hello", "/db"]
	})

@app.route("/hello")
def hello():
	return jsonify({"message": "Hello World"})

@app.route("/db")
def db_check():
	try:
		conn = get_db_connection()
		cursor = conn.cursor(dictionary=True)
		
		cursor.execute("SELECT name, email FROM users")
		rows = cursor.fetchall()
		cursor.close()
		conn.close()

		return jsonify({
			"db_status": "OK", 
			"users": rows
		})

	except Exception as e:
		return jsonify({
			"db_status": "ERROR",
			"error": str(e)
		}), 500

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000)
