"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system("dropdb planetMe")
os.system("createdb planetMe")

model.connect_to_db(server.app)
model.db.create_all()

mj = crud.create_user("michael_jackson@gmail.com","heehee87","Michael")
crud.create_journal(mj.user_id,"1/3/2023","10:45","Happy","I am feeling good today")

