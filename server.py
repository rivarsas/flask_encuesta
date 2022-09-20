from flask import Flask, render_template, request, redirect, session, flash
import survey
from termcolor import cprint
app = Flask(__name__)
app.secret_key = "ELPEPE"


@app.route("/")
def root():
    return render_template("index.html")


@app.route("/process", methods=["POST"])
def process():
    cprint(request.form,"red")

    session["name"] = request.form["name"]
    session["location"] = request.form["location"]
    session["language"] = request.form["language"]
    session["comments"] = request.form["comments"]

    formulario={
        "name":request.form["name"],
        "location":request.form["location"],
        "language":request.form["language"],
        "comments":request.form["comments"]
    }
    if(survey.Survey.validateSurvey(formulario)):
        return redirect("/result")
    else:
        return redirect("/")


@app.route("/result")
def result():
    return render_template("result.html")


if(__name__ == "__main__"):
    app.run(debug=True)
