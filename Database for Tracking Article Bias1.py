
5.1 Database for Tracking Article Bias

A Python Flask API can handle database operations:

from flask import Flask, request, jsonify

import psycopg2

app = Flask(__name__)

conn = psycopg2.connect("dbname=bias_db user=postgres password=yourpassword")

cursor = conn.cursor()

@app.route("/save_analysis", methods=["POST"])

def save_analysis():

    data = request.json

    cursor.execute("INSERT INTO articles (url, content, sentiment_score, biased_words) VALUES (%s, %s, %s, %s) ON CONFLICT (url) DO NOTHING",
                   (data["url"], data["content"], data["sentiment_score"], data["biased_words"]))

    conn.commit()

    return jsonify({"message": "Data saved"}), 201

if __name__ == "__main__":

    app.run(debug=True)


This API allows storing and retrieving analyzed articles.

