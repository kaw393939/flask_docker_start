from application.database import User, db
from faker import Faker


def test_add_users(app):

    faker = Faker('en')
    user_list = []
    number_of_users = 300
    with app.app_context():

        for i in range(number_of_users):
            user = User()
            user.name = faker.name()
            user.password = faker.password()
            user.email = faker.email()
            user.phone = faker.phone_number()
            user.address = faker.address()
            user_list.append(user)

        db.session.add_all(user_list)
        db.session.commit()
    assert db.session.query(User).count() == number_of_users