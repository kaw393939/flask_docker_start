

from application.database import User, db


def test_index_route(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"My Homepage" in response.data


def test_add_users(app):
    from faker import Faker

    faker = Faker('en')
    user_list = []
    number_of_users = 300
    with app.app_context():

        for i in range(number_of_users):
            user = User()
            user.name = faker.name()
            user.password = faker.password()
            user_list.append(user)

        db.session.add_all(user_list)
        db.session.commit()
    assert db.session.query(User).count() == number_of_users
