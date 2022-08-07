from flask import Flask

app = Flask(__name__)

@app.route("/members")
def members():
    return {"members": ["member1", "2", "3"]}

if __name__ == "__main":
    app.run(debug = True)
