from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello! VERSION 4 - This one used Recreate strategy!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
