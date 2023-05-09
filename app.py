from flask import Flask, request, render_template, flash
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as SURVEY

RESPONSE_KEY = "response"

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

debug = DebugToolbarExtension(app)

@app.route('/')
def start_survey():
    return render_template('survey_start.html')