from flask import Flask, request, render_template, flash, redirect, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"

debug = DebugToolbarExtension(app)
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False

RESPONSES_KEY = "response"
CURRENT_QUESTION = "active"

@app.route("/")
def start_survey():
    session[CURRENT_QUESTION]= 0
    return render_template("/surveyStart.html", survey=survey)

@app.route("/begin", methods=["POST"])
def redirect_to_questions():
    session[RESPONSES_KEY]= []
    return redirect("/question/0")

@app.route("/question/<int:questionID>")
def show_questions(questionID):
    responses = session[RESPONSES_KEY]
    current_question = session[CURRENT_QUESTION]

    if len(responses) == len(survey.questions):
        return redirect("/completed")
    
    elif current_question == False:
        return redirect("/")
    
    elif len(responses) != questionID:
        flash(f"Invalid question id: {questionID}.")
        return redirect(f'/question/{len(responses)}')

    current_question = questionID
    question = survey.questions[questionID]
    return render_template(f"question.html", question=question, question_num = questionID)

@app.route("/answer", methods=["POST"])
def answer():
    session[RESPONSES_KEY].append(request.form["answer"])

    if len(survey.questions) == session[CURRENT_QUESTION]:
        return redirect("completed.html")
    
    return redirect(f"/question/{len(session[RESPONSES_KEY])}")

@app.route("/completed")
def load_completed():
    return render_template("completed.html")
