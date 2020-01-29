from flask import Flask, request, redirect, url_for, render_template
from flask import session as login_session
from model import User
from databases import *

app = Flask(__name__)
app.secret_key = "MY_SUPER_SECRET_KEY"


@app.route("/")
def home_page():
	return render_template("home.html")



@app.route("/superman", methods= ['GET', 'POST'])
def superman_page():
	if request.method == "POST":
		if request.form['superman']=="superman":
			Superman.votes += 1
		return render_template('home.html')
	return render_template("superman.html")

@app.route("/batman", methods= ['GET', 'POST'])
def batman_page():
	if request.method == "POST":
		if request.form['batman']=="batman":
			Batman.votes += 1
		return render_template('home.html')
	return render_template("batman.html")

@app.route("/allmight" , methods= ['GET', 'POST'])
def allmight_page():
	if request.method == "POST":
		if request.form['allmight']=="allmight":
			Allmight.votes += 1
		return render_template('home.html')
	return render_template("allmight.html")

@app.route("/spiderman", methods= ['GET', 'POST'])
def spiderman_page():
	if request.method == "POST":
		if request.form['spiderman']=="spiderman":
			Spiderman.votes += 1
		return render_template('home.html')
	return render_template("spiderman.html")

@app.route("/ironman", methods= ['GET', 'POST'])
def ironman_page():
	if request.method == "POST":
		if request.form['ironman']=="ironman":
			Ironman.votes += 1
		return render_template('home.html')
	return render_template("ironman.html")	

@app.route("/signup_login", methods= ['GET', 'POST'])
def signup_page():
	if request.method == "POST":
		 user = add_user(request.form['username'],request.form['password'])
		 return render_template("home.html", user=user)
	return render_template("signup.html")
		


if __name__ == '__main__':
	app.run(debug=True)