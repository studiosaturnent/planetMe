from flask import Flask, render_template
from flask import url_for


#From flask import Flask, render_template, redirect, session

app = Flask(__name__)

# @app.route("/")
# def index():
#    return render_template("homepage.html")

@app.route("/")
def view_home():
    return render_template("base.html", title="Home page")

@app.route("/journal")
def view_first_page():
    return render_template("journal.html", title="Journal")

@app.route("/dashboard/")
def view_second_page():
    return render_template("dashboard.html", title="Dashboard")

@app.route('/homepage')
def homepage():
   return render_template("homepage.html")


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

with app.test_request_context():
    print(url_for('homepage'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))

# @app.route('/dashboard/')
# @app.route('/hello/<name>')
# def dashboard(name="Monie"):
#     return render_template('dashboard.html', name=name)

# @app.route('/journal')
# def journal_home():
#     return render_template('journal.html')    


# app.route('/login', methods=[“POST”,”GET”])
# def login_user():

# 	user_email = request.form.get(“user_email”)
# 	user = crud.get_journals(“user_email”) 
# 	#returns a user object or none
	
# 	if user is None:
# 		return redirect(“/”)
# 	else:
# 		session[“user_id”] = user.user_id
# 		session[“user_name”] = user.user_name	
# 	return render_template(“some.html”)

# app.route(“profile”)
# def profile










# //Session [‘user_id”] = “Sacalatoo Decaltoo”
# 	// id is put in session 