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


@app.route("/journal", methods=['GET'])
def view_journal():
#displaying whole journal table for user 
    user_id = session.get("user_id")
    user = crud.get_user(user_id)

    return render_template("journal.html", title="Journal", journals=user.journals)


@app.route("/new_entry")
def new_entry_viewer():
    return render_template("new_entry.html", title="New Entry")

@app.route("/new_entry", methods =["POST"])
def new_entry():
#adding new entry to journal table
    user_id = session.get("user_id")
    date = request.form.get('date')
    time = request.form.get('time')
    mood = request.form.get('mood')
    body_data = request.form.get('body')
    crud.create_journal(user_id=user_id, date=date, time=time, mood=mood , body_data=body_data )


    return redirect("/journal")

@app.route("/view_entry/<journal_id>")
def view_entry(journal_id):
#viewing a specific entry from table by entry_id
    journal = crud.get_entry_by_id(journal_id)
    return render_template("view_entry.html", title="View Entry", journal=journal)    


@app.route("/dashboard/")
def view_dashboard():
#view user.name from users table
    user_id = session.get("user_id")
    user = crud.get_user(user_id)

    return render_template("dashboard.html", title="Dashboard", user = user)


@app.route('/login', methods=['GET'])
def login_page(): 
#return login template page
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login_post():
#log user in from users table data
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

@app.route('/register')
def register():
#creating user to update users table
    # email = request.form.get('email')
    # print(email)
    # password = request.form.get('password')
    # print(password)
    # name = request.form.get('name')
    # print(name)
    # user = crud.get_create_user(email)
    
    # if user != None and password == user.password:
    #     session["user_id"] = user.user_id
    #     return redirect("/dashboard")
    # else:
    #     return redirect("/register")

   return render_template("register.html")   



if __name__ == "__main__":
    from model import connect_to_db

    connect_to_db(app)

    app.run(debug=True, host="0.0.0.0",port=5001)









# //Session [‘user_id”] = “Sacalatoo Decaltoo”
# 	// id is put in session 