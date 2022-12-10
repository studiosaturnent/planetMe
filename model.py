# """Data model for journals."""

# from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()

# #---------------------------------------------------------------------#

# class Journal(db.Model):
#     """Map points for journals."""

#     __tablename__ = "journals"

#     user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
#     journal_id = db.Column(db.String(64), nullable=True)
#     gender = db.Column(db.String(64), nullable=True)
#     birth_year = db.Column(db.String(64), nullable=True)


#     def __init__(self,
#                  id,
#                  user_id,
#                  name,):

#         """Create a journal."""

#         self.id = id
#         self.user_id = user_id
#         self.name = name


#     def __repr__(self):
#         """Clear representation of Journal."""

#         repr_str = "<Journal user_id={user_id}>"

#         return repr_str.format(user_id=self.journal_id)



# class Entry(db.Model):
#     """Map points for journal entries."""

#     __tablename__ = "entry"

#     user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
#     date = db.Column(db.Date(64), nullable=True)
#     time = db.Column(db.TimeStamp(64), nullable=True)
#     mood = db.Column(db.Varchar(64), nullable=True)
#     body = db.Column(db.String(64), nullable=True)



#     def __init__(self,
#                  id,
#                  user_id,
#                  date,
#                  mood,
#                  body ):

#         """Create a journal."""

#         self.id = id
#         self.user_id = user_id
#         self.date = date
#         self.mood = mood
#         self.body = body



#     def __repr__(self):
#         """Clear representation of Entry."""

#         repr_str = "<Entry user_id={user_id}>"

#         return repr_str.format(user_id=self.journal_id)


# #---------------------------------------------------------------------#

# def connect_to_db(app):
#     """Connect the database to Flask app."""

#     app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///users'
#     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#     db.app = app
#     db.init_app(app)


# if __name__ == "__main__":
#     from server import app
#     connect_to_db(app)
#     print("Connected to DB.")
