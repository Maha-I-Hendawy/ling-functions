from functions import clean_words, find_prefix, find_suffix, find_pronoun
from text import Text
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
	if request.method == 'POST':
		text = request.form['text']
		t = Text(text)
		clean_words(t.words())
	return render_template("home.html")




