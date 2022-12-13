"""Models for movie ratings app."""

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """A user."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)

    entries = db.relationship("Entries", back_populates="user")

    def __repr__(self):
        return f"<User user_id={self.user_id} email={self.email}>"


class Journals(db.Model):
    """A journal."""

    __tablename__ = "journals"

    journal_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.VarChar)
    date = db.Column(db.Date)
    time = db.Column(db.Time)
    mood = db.Column(db.VarChar)
    body_data = db.Column(db.String)

    entry = db.relationship("Entries", back_populates="journal")

    def __repr__(self):
        return f"<Journals journal_id={self.journal_id} name={self.name}>"


class Entries(db.Model):
    """A journal entry."""

    __tablename__ = "entries"

    rating_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    score = db.Column(db.Integer)
    movie_id = db.Column(db.Integer, db.ForeignKey("movies.movie_id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))

    movie = db.relationship("Movie", back_populates="ratings")
    user = db.relationship("User", back_populates="ratings")

    def __repr__(self):
        return f"<Rating rating_id={self.rating_id} score={self.score}>"


def connect_to_db(flask_app, db_uri="postgresql:///ratings", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)






from flask_sqlalchemy import SQLAlchemy

db = Journals()

def connect_to_db(app, db_name):
    """Connect to database."""

    app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql:///{journals}"
    app.config["SQLALCHEMY_ECHO"] = True
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = app
    db.init_app(app,"journals")

class Journal(db.Model):
    """Journal with data columns."""

    __tablename__ = "journals"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    date = db.Column(db.Date(64), nullable=True)
    time = db.Column(db.TimeStamp(64), nullable=True)
    mood = db.Column(db.Varchar(64), nullable=True)
    body = db.Column(db.String(64), nullable=True)

def __repr__(self):
    """Show info about journal."""

    return f"<Journal id={self.journal_id} name={self.name}>"

@classmethod
def get_journal_entries():
    """Get all journal records."""

    return self.date.all()




# # """Data model for journals."""

# # from flask_sqlalchemy import SQLAlchemy
# from . import db
# from flask_login import UserMixin

# # db = SQLAlchemy()

# # #---------------------------------------------------------------------#

# # class Journal(db.Model):
# #     """Map points for journals."""

# #     __tablename__ = "journals"

# #     id = db.Column(db.Integer, primary_key=True)
# #     journal_id = db.Column(db.String(64), nullable=True)

# class User(db.Model, UserMixin):
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(150), unique=True)
#     password = db.Column(db.String(150))
#     first_name = db.Column(db.String(150))

# #     def __init__(self,
# #                  id,
# #                  journal_id,
# #                  name,):

# #         """Create a journal."""

# #         self.id = id
# #         self.user_id = user_id
# #         self.name = name


# #     def __repr__(self):
# #         """Clear representation of Journal."""

# #         repr_str = "<Journal user_id={user_id}>"

# #         return repr_str.format(user_id=self.journal_id)



# # class Entry(db.Model):
# #     """Map points for journal entries."""

# #     __tablename__ = "entry"

# #     user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
# #     date = db.Column(db.Date(64), nullable=True)
# #     time = db.Column(db.TimeStamp(64), nullable=True)
# #     mood = db.Column(db.Varchar(64), nullable=True)
# #     body = db.Column(db.String(64), nullable=True)





# #     def __init__(self,
# #                  id,
# #                  user_id,
# #                  date,
# #                  mood,
# #                  body ):

# #         """Create a journal."""

# #         self.id = id
# #         self.user_id = user_id
# #         self.date = date
# #         self.mood = mood
# #         self.body = body



# #     def __repr__(self):
# #         """Clear representation of Entry."""

# #         repr_str = "<Entry user_id={user_id}>"

# #         return repr_str.format(user_id=self.journal_id)


# # #---------------------------------------------------------------------#

# # def connect_to_db(app):
# #     """Connect the database to Flask app."""

# #     app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///users'
# #     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# #     db.app = app
# #     db.init_app(app)


# # if __name__ == "__main__":
# #     from server import app
# #     connect_to_db(app)
# #     print("Connected to DB.")
