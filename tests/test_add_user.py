from application.database import User, db
from faker import Faker


def test_add_users(app, create_300_users):

    assert db.session.query(User).count() == 300