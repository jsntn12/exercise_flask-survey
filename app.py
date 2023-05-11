from flask import Flask, request, render_template, flash, redirect
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey


responses = []

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"

debug = DebugToolbarExtension(app)
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False

current_question= {"active" : None}

CURRENT_INDEX = current_question['active']

@app.route("/")
def start_survey():
    current_question['active']= 0

    return render_template("/surveyStart.html", survey=survey)

@app.route("/begin", methods=["POST"])
def redirect_to_questions():
    return redirect("/question/0")

@app.route("/question/<int:questionID>")
def show_questions(questionID):

    if len(responses) == len(survey.questions):
        return redirect("/completed")
    
    elif current_question['active'] == None:
        return redirect("/")
    
    elif len(responses) != questionID:
        flash(f"Invalid question id: {questionID}.")
        return redirect(f'/question/{len(responses)}')

    current_question["active"] = questionID
    
    print(f"Survery length is {len(survey.questions) }This is the question ID {questionID}, Status of obj {current_question['active'] }")
    question = survey.questions[questionID]

    return render_template(f"question.html", question=question, question_num = questionID)

@app.route("/answer", methods=["POST"])
def answer():
    responses.append(request.form["answer"])
    if len(survey.questions) == current_question['active']:
        return redirect("completed.html")
    return redirect(f"/question/{len(responses)}")






# app.route("/completed")
@app.route("/completed")
def load_completed():
# load thank you for completing the page 
    return render_template("completed.html")
