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
    # establish count to keep track of the question number asked 
    return redirect("/question/0")

@app.route("/question/<int:questionID>")
def show_questions(questionID):

    #if the len of response == questions return completed page 
    if len(response) == len(survey.questions):
        return redirect("/completed")
    
    # corner case - user trying to access question out of order 
    # corner case answer question before the start button 

    # render template the page with the question using current count of questions 


# app.route("/completed")
@app.route("/completed")
def load_completed():
# load thank you for completing the page 
    return render_template("completed.html")
