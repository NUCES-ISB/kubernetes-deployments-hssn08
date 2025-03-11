import os
import psycopg2
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    # Retrieve environment variables
    db_user = os.getenv("POSTGRES_USER", "postgres")
    db_password = os.getenv("POSTGRES_PASSWORD", "password")
    db_host = os.getenv("POSTGRES_HOST", "localhost")
    db_name = os.getenv("POSTGRES_DB", "flaskdb")

    try:
        conn = psycopg2.connect(
            user=db_user, 
            password=db_password,
            host=db_host,
            port=5432,
            database=db_name
        )
        cur = conn.cursor()
        cur.execute("SELECT version();")
        version = cur.fetchone()
        cur.close()
        conn.close()
        return jsonify(message="Connected to Postgres!", version=version)
    except Exception as e:
        return jsonify(error=str(e))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)