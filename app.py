from flask import Flask, request, render_template, flash, redirect
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

response = []

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"

debug = DebugToolbarExtension(app)
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False

@app.route("/")
def start_survey():

    return render_template("surveyStart.html", survey=survey)

@app.route("/begin", methods=["POST"])
def redirect_to_questions():
    return redirect("/question/0")

@app.route("/question/<int:questionID>")
def show_questions(questionID):
    if len(response) == len(survey.questions):
        return redirect("/completed")

