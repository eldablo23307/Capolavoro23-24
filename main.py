from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/user<user>")
def user(user):
    text = escape(user)
    return render_template("chat.html.jinja", user_name=text)

if __name__ == "__main__":
    app.run()