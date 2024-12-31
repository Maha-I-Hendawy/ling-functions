from functions import clean_words, find_prefix, find_suffix, find_pronoun
from text import Text
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SECRET_KEY'] = '254404398d8dc06763d87716e363'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ling.db'
app.config['SQLALCHEMY_DATABASE_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
app.app_context().push()


class TEXT(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	text = db.Column(db.Text)

	def __str__(self):
		return f"{self.text}"

@app.route('/', methods=['GET', 'POST'])
def home():
	mytext = TEXT.query.all()
	texts = [t.text for t in mytext]
	
	if request.method == 'POST':
		text = request.form['text']
		text1 = TEXT(text=text)
		db.session.add(text1)
		db.session.commit()
		return redirect(request.url)
		
	return render_template("home.html", mytext=mytext)




