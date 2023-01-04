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

crud.create_user("simone@gmail.com","password","simone")
crud.create_journal("1/3/2023","10:45"," ","I am feeling good today")

