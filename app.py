from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Merhaba, bu benim ilk web sitem!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
