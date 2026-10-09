from flask import Flask, send_from_directory, jsonify
from pathlib import Path

app = Flask(__name__, static_folder=None)
BASE_DIR = Path(__file__).resolve().parent

@app.get("/")
def home():
    return send_from_directory(BASE_DIR, "index.html")

@app.get("/health")
def health():
    return jsonify(status="ok", app="APEX DRIVE 3D")

@app.get("/<path:filename>")
def static_files(filename):
    # Only serve files inside this project directory.
    target = (BASE_DIR / filename).resolve()
    if BASE_DIR not in target.parents and target != BASE_DIR:
        return jsonify(error="Not found"), 404
    if target.is_file():
        return send_from_directory(BASE_DIR, filename)
    return jsonify(error="Not found"), 404
