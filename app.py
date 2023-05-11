from flask import Flask, request, render_template, flash, redirect
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

responses = []

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"

debug = DebugToolbarExtension(app)
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False

current_question= {"active" : None}

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
    # elif len(response) == 0:
    #     return redirect("/")
    # elif len(response) != current_question:
    #     return redirect(f"/question/{current_question}")

    print(f"This is the question ID {questionID}, Status of obj {current_question['active'] }")
    current_question["active"] = questionID
    question = survey.questions[questionID]

    return render_template(f"question.html", question=question, question_num = questionID)

@app.route("/answer", methods=["POST"])
def answer():
    choice = request.form['answer']
    responses.append(request.form["answer"])

    return redirect(f"/question/{len(responses)}")
    # update the current question to + 1
    # get the input 
    # save the ansewr to array 





# app.route("/completed")
@app.route("/completed")
def load_completed():
# load thank you for completing the page 
    return render_template("completed.html")
