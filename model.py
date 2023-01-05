"""Models for journal app."""

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()



class User(db.Model):
    """A user."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, nullable=False, autoincrement=True, primary_key=True)
    email = db.Column(db.String, unique=True , nullable=False)
    password = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)


    journals = db.relationship("Journal", back_populates="user")

    def __repr__(self):
        return f"<User user_id={self.user_id} email={self.email}>"


class Journal(db.Model):
    """A journal."""

    __tablename__ = "journal"

    journal_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    date = db.Column(db.DateTime)
    time = db.Column(db.Time)
    mood = db.Column(db.String)
    body_data = db.Column(db.String)

    user = db.relationship("User", back_populates="journals")


    def __repr__(self):
        return f"<Journal journal_id={self.journal_id} date={self.date} time={self.time} mood={self.mood} body_data={self.body_data}>"




def connect_to_db(app, database_name="planetMe"):
    """Connect to database."""

    app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql:///{database_name}"
    app.config["SQLALCHEMY_ECHO"] = True
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


    db.app = app
    db.init_app(app)





