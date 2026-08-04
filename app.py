from flask import Flask, render_template, request, send_from_directory, jsonify
import os
import subprocess

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "output"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():

    if "video" not in request.files:
        return "No file uploaded."

    file = request.files["video"]

    if file.filename == "":
        return "No file selected."

    upload_path = os.path.join(UPLOAD_FOLDER, "input.mp4")

    file.save(upload_path)

    # Reset processing status
    with open(os.path.join(OUTPUT_FOLDER, "status.txt"), "w") as f:
        f.write("processing")

    # Start detector in background
    subprocess.Popen(["python3", "detector.py"])

    # Immediately show processing page
    return render_template("processing.html")


@app.route("/status")
def status():

    status_file = os.path.join(OUTPUT_FOLDER, "status.txt")

    if not os.path.exists(status_file):
        return jsonify({"finished": False})

    with open(status_file, "r") as f:
        state = f.read().strip()

    return jsonify({"finished": state == "done"})


@app.route("/result")
def result():
    return render_template("result.html")


@app.route("/output/<filename>")
def output_video(filename):
    return send_from_directory(OUTPUT_FOLDER, filename)


if __name__ == "__main__":
    app.run(debug=True)