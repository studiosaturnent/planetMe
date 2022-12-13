"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system("dropdb journals")
os.system("createdb journals")

model.connect_to_db(server.app)
model.db.create_all()

# Load number sequence data from JSON file
with open("data/number_defs.json") as f:
    number_data = json.loads(f.read())
    
# Load number sequence data from JSON file
with open("data/number_defs.json") as f:
    number_data = json.loads(f.read())
# Create movies, store them in list so we can use them
# to create fake ratings
journals_in_db = []
for journal in jouranal_data:
    title, overview, poster_path = (
        journal["title"],
        movie["overview"],
        movie["poster_path"],
    )
    release_date = datetime.strptime(movie["release_date"], "%Y-%m-%d")

    db_movie = crud.create_movie(title, overview, release_date, poster_path)
    movies_in_db.append(db_movie)

model.db.session.add_all(movies_in_db)
model.db.session.commit()

# Create 10 users; each user will make 10 ratings
for n in range(10):
    email = f"user{n}@test.com"  # Voila! A unique email!
    password = "test"

    user = crud.create_user(email, password)
    model.db.session.add(user)

    for _ in range(10):
        random_movie = choice(movies_in_db)
        score = randint(1, 5)

        rating = crud.create_rating(user, random_movie, score)
        model.db.session.add(rating)

model.db.session.commit()