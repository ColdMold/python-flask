from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/assignment10.html', methods=["GET","POST"])

def formSubmitted():
	fname = None
	lname = None
	guess = None
	number = None
	
	randomNum = random.randint(1,5)
		

	if "fname" in request.args:
		fname = request.args["fname"]
	if "lname" in request.args:
		lname = request.args["lname"]
	if "guess" in request.form:
		guess = request.form["guess"]
	if "number" in request.form:
		number = request.form["number"]
		

	return render_template('assignment10.html', fname=fname, lname=lname, randomNum=randomNum, guess=guess, number=number)

