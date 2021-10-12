import os
from flask import Flask, render_template  # import a class Flask from flask


# create an instance of Flask class and store it in app variable (customary)
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/careers")
def careers():
    return render_template("careers.html")


if __name__ == "__main__":  # __main__ is python main module
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
# DO NOT set to True when in production or when submitting the project as it
# leads to vulnerabilities!
