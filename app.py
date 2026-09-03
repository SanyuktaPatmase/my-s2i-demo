from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello! VERSION 2 - This proves BuildConfig and ImageStream work together!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
