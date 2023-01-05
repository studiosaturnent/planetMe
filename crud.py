"""CRUD operations."""

from model import db, User, Journal, connect_to_db


def create_user(email, password, name):
    """Create and return a new user."""

    user = User(email=email, password=password, name=name)
    db.session.add(user)
    db.session.commit()
    return user


def get_users():
    """Return all users."""

    return User.query.all()


def get_user_by_id(user_id):
    """Return a user by primary key."""

    return User.query.get(user_id)


def get_user_by_email(email):
    """Return a user by email."""

    return User.query.filter(User.email == email).first()


def create_journal(user_id, date, time, mood , body_data ):
    """Create and return a new Journal object."""
    
    entry = Journal(
        user_id = user_id,
        date=date,
        time=time,
        mood=mood,
        body_data=body_data
    )
    db.session.add(entry)
    db.session.commit()

    return entry

def get_user(user_id):
    """Find and display a user's name."""

    return User.query.get(user_id)


def get_journal():
    """Return all journals."""

    return Journal.query.all()


def get_entry_by_id(journal_id):
    """Return a journal by primary key."""

    return Journal.query.get(journal_id)





if __name__ == "__main__":
    from server import app

    connect_to_db(app)
