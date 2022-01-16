from lib2to3.pgen2.pgen import generate_grammar
from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import *

app = Flask(__name__)

app.config['SECRET_KEY'] = "madlibs"
debug = DebugToolbarExtension(app)

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/<phrase>')
def show_story_form(phrase):
    prompts = eval(phrase).prompts
    title = phrase.title().replace('_', ' ')
    return render_template('form-2.html', prompts=prompts, phrase=phrase, title=title)

@app.route('/<phrase>/story')
def show_story(phrase):
    answers = dict(request.args)
    title = phrase.title().replace('_', ' ')
    madlib = eval(phrase).generate(answers)
    return render_template("story.html", madlib=madlib, title=title)
