from flask import Flask # import a class Flask from flask
import os

app = Flask(__name__) # create an instance of Flask class and 
                     # store it in app variable (customary)

@app.route("/")
def index():
    return "Hello World!"


if __name__ == "__main__": #__main__ is python main module
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True) #DO NOT set to True when in production or when submitting the project as it leads to vulnerabilities!
