from flask import Flask, render_template, redirect, request, session
from flask import url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


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


@app.route('/login', methods=['GET', 'POST'])
def login():
    print(request.method)
    if request.method == 'POST':
        if request.form.get('Encrypt') == 'Encrypt':
                # pass
                redirect ("Encrypted")
        elif  request.form.get('Decrypt') == 'Decrypt':
                # pass # do something else
                print("Decrypted")
        else:
                # pass # unknown
                return redirect("/dashboard")
    elif request.method == 'GET':
            # return render_template("index.html")
            print("No Post Back Call")  

    return render_template('login.html')

@app.route('/dashboard/<username>')
def profile(username):
    return f'{username}\'s profile'

with app.test_request_context():
    print(url_for('homepage'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))

@app.route('/dashboard/')
@app.route('/dashboard/<name>')
def dashboard(name="Monie"):
    return render_template('dashboard.html', name=name)


if __name__ == "__main__":
    from model import connect_to_db

    connect_to_db(app, "planetMe")

    app.run(debug=True, host="0.0.0.0")









# //Session [‘user_id”] = “Sacalatoo Decaltoo”
# 	// id is put in session 