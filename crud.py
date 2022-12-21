"""CRUD operations."""

from model import db, User, Journal, Entry, connect_to_db


def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

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


def create_journal(date, time, mood , body_data ):
    """Create and return a new Journal object."""

    journal = Journals(
        date=date,
        time=time,
        mood=mood,
        body_data=body_data,
    )

    return journal


def get_journal():
    """Return all journals."""

    return Journals.query.all()


def get_entry_by_id(journal_id):
    """Return a journal by primary key."""

    return Journals.query.get(journal_id)


def create_entry(user, journal):
    """Create and return a new entry."""

    entry = Entries(user=user, journal=journal)

    return entry


def update_entry(entry_id, new_entry):
    """ Update a rating given rating_id and the updated score. """
    entry = Entries.query.get(entry_id)
    entry.score = new_entry

if __name__ == "__main__":
    from server import app

    connect_to_db(app)
