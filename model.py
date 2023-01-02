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


   # journals = db.relationship("Journal", back_populates="user")

    def __repr__(self):
        return f"<User user_id={self.user_id} email={self.email}>"


class Journal(db.Model):
    """A journal."""

    __tablename__ = "journals"

    journal_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
   # entry = db.relationship("Entry", back_populates="journal")

    def __repr__(self):
        return f"<Journals journal_id={self.journal_id} name={self.name}>"


class Entry(db.Model):
    """A journal entry."""

    __tablename__ = "entries"

    journal_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    entry_id = db.Column(db.Integer)
    date = db.Column(db.DateTime)
    time = db.Column(db.Time)
    mood = db.Column(db.String)
    body_data = db.Column(db.String)

    def __repr__(self):
        return f"<Entry entry_id={self.entry_id}>"


def connect_to_db(app, database_name="planetMe"):
    """Connect to database."""

    app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql:///{database_name}"
    app.config["SQLALCHEMY_ECHO"] = True
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


    db.app = app
    db.init_app(app)





