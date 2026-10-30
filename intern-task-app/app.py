from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from the Intern Take-Home App running in Kubernetes!"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)