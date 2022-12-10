# """Load journal data into database."""

# from model import Journal, connect_to_db, db
# from server import app

# #---------------------------------------------------------------------#



# def get_journals():
#     """Load journals from dataset into database."""

#     with open("data/journal_data.csv") as carriage_data:
#         for i, row in enumerate(journal_data):
#             if i >= 50:
#                 break

#             db.session.add(User(*row.rstrip().split(",")))


#     db.session.commit()

# #---------------------------------------------------------------------#

# if __name__ == '__main__':
#     connect_to_db(app)
#     db.create_all()

#     get_users()
