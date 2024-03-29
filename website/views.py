from flask import Flask, render_template, request, jsonify
from sklearn.externals import joblib
import pandas as pd
import praw
import reddit_cred

app=Flask(__name__)

@app.route('/')
def index():
	return render_template("layout.html")

reddit=praw.Reddit(client_id='1ImKqf0xxFG6ZA',
					client_secret=reddit_cred.client_secret,
					user_agent='Udit',
					username='uBoy2000', password=reddit_cred.password
					)

@app.route('/output/',methods=['POST'])
def output():
	t=request.form.get('url',0)
	a=reddit.submission(url=t)
	value=a.title
	sgd_from_joblib=joblib.load('model.pkl')

	ndf=pd.DataFrame(
		{
			'Title': [value]
		}
	)
	Test=ndf.Title
	w=sgd_from_joblib.predict(Test)
	data = {'flair': w[0]}
	data = jsonify(data)
	return data

if __name__=="__main__":
	app.run()	
