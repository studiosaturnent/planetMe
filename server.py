from flask import Flask, flash, render_template, redirect, request, session
from random import choice
from flask import url_for
from model import db
from flask_sqlalchemy import SQLAlchemy
import crud


app = Flask(__name__)

app.secret_key = 'A SECRET KEY'

QUOTES = [
    "All our dreams can come true, if we have the courage to pursue them. —Walt Disney",
    "The secret of getting ahead is getting started. —Mark Twain",
    "Write it. Shoot it. Publish it. Crochet it. Sauté it. Whatever. MAKE. —Joss Whedon",
    "Everything you can imagine is real.”―Pablo Picasso",
    "Its no use going back to yesterday, because I was a different person then.” ―Lewis Carroll",
    "Happiness is not something ready made. It comes from your own actions.” ―Dalai Lama XIV",
    "Impossible is just an opinion. —Paulo Coelho",
    "If you hear a voice within you say, You cannot paint, then by all means paint, and that voice will be silenced. ―Vincent Van Gogh",
    "Very often, a change of self is needed more than a change of scene. ―A.C. Benson",
    "Trust yourself that you can do it and get it. ―Baz Luhrmann.",
    "It’s not the load that breaks you down, it’s the way you carry it. ―Lou Holtz",
    "Keep your eyes on the stars, and your feet on the ground. ―Theodore Roosevelt",
    "Work hard in silence, let your success be the noise. ―Frank Ocean",
]

@app.route("/")
def view_home():
    compliment = choice(QUOTES)

    return render_template("homepage.html", title="Home page", compliment=compliment)
    
@app.route('/homepage')
def homepage():

   return render_template("homepage.html")


@app.route("/journal", methods=['GET'])
def view_journal():
#displaying whole journal table for user 
    compliment = choice(QUOTES)
    user_id = session.get("user_id")
    user = crud.get_user(user_id)

    return render_template("journal.html", title="Journal", journals=user.journals, user = user, compliment=compliment)


@app.route("/new_entry")
def new_entry_viewer():
    compliment = choice(QUOTES)
    return render_template("new_entry.html", title="New Entry", compliment=compliment)

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
    compliment = choice(QUOTES)
    journal = crud.get_entry_by_id(journal_id)
    return render_template("view_entry.html", title="View Entry", journal=journal,compliment=compliment)    


@app.route("/dashboard/")
def view_dashboard():
#view user.name from users table   

    user_id = session.get("user_id")
    user = crud.get_user(user_id)
    compliment = choice(QUOTES)

    return render_template("dashboard.html", title="Dashboard", user = user, compliment=compliment)


@app.route('/login', methods=['GET'])
def login_page(): 
#return login template page
    compliment = choice(QUOTES)
    return render_template('login.html', compliment=compliment)


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
        return redirect("/dashboard/")
    else:
        flash("Invalid Credentials, Please Try Again")
        return redirect("/login")

@app.route('/logout', methods=['GET'])
def log_out(): 
#return login template page
    return render_template('login.html')        

@app.route('/register',methods=['GET'])
def register_page():
#creating register page
   compliment = choice(QUOTES)

   return render_template("register.html", compliment = compliment)   

@app.route('/register',methods=['POST'])
def register_crud():
#creating register page
    email = request.form.get('email')
    print(email)
    password = request.form.get('password')
    print(password)
    name = request.form.get('name')
    print(name)
    user = crud.get_user_by_email(email)
    
    
    if user:
      flash("User Already exists")
    else:
        user = crud.create_user(email,password,name)
        db.session.add(user)
        db.session.commit() 
        session["user_id"] = crud.get_user(email).user_id

   
    return redirect("/dashboard/")

# function showFortune() {
#   fetch('/fortune')
#     .then((response) => response.text())
#     .then((fortune) => {
#       document.querySelector('#fortune-text').innerHTML = fortune;
#     });

# function changeColor() {
#   const colorChangeEls = document.querySelectorAll('.color-change');

#   for (const el of colorChangeEls) {
#     el.classList.add('red');
#   }
# }    
# }

# document.querySelector('#get-fortune-button').addEventListener('click', showFortune);

# // PART 2: SHOW WEATHER

# function showWeather(evt) {
#   evt.preventDefault();
#   const zipcode = document.querySelector('#zipcode-field').value;
#   const url = `/weather?zipcode=${zipcode}`;
#   fetch(url)
#     .then((response) => response.json())
#     .then((jsonData) => {
#       document.querySelector('#weather-info').innerText = jsonData.forecast;
#     });
# }

if __name__ == "__main__":
    from model import connect_to_db

    connect_to_db(app)

    app.run(debug=True, host="0.0.0.0",port=5001)
 