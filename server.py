from flask import Flask, render_template, redirect, request, session
from flask import url_for
from flask_sqlalchemy import SQLAlchemy
import crud


app = Flask(__name__)

app.secret_key = 'A SECRET KEY'


@app.route("/")
def view_home():
    return render_template("homepage.html", title="Home page")
    
@app.route('/homepage')
def homepage():
   return render_template("homepage.html")

@app.route("/journal")
def view_first_page():
    return render_template("journal.html", title="Journal")

@app.route("/dashboard/")
def view_second_page():
    return render_template("dashboard.html", title="Dashboard")


@app.route('/login', methods=['GET'])
def login_page(): 

    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login_post():

    email = request.form.get('email')
    print(email)
    password = request.form.get('password')
    print(password)
    user = crud.get_user_by_email(email)
    
    if user != None and password == user.password:
        session["user_id"] = user.user_id
        return redirect("/dashboard")
    else:
        return redirect("/login")

@app.route('/dashboard/<name>')
def profile(name):
    return f'{name}\'s profile'





if __name__ == "__main__":
    from model import connect_to_db

    connect_to_db(app)

    app.run(debug=True, host="0.0.0.0",port=5001)









# //Session [‘user_id”] = “Sacalatoo Decaltoo”
# 	// id is put in session 