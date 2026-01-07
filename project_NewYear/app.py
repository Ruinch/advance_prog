import os
import sys
from flask import Flask, render_template
import webbrowser
from threading import Timer

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

app = Flask(
    __name__,
    template_folder=resource_path("templates"),
    static_folder=resource_path("static")
)

@app.route("/")
def index():
    return render_template("index.html")

def open_browser():
    webbrowser.open("http://127.0.0.1:5000")

if __name__ == "__main__":
    Timer(1, open_browser).start()
    app.run(debug=False)
