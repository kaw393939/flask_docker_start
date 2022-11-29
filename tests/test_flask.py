from faker import Faker

from application.database import User, db


def test_index_route(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"My IS601" in response.data


def test_about_route(client):
    response = client.get("/about")
    assert response.status_code == 200
    assert b"About" in response.data


def test_users_route(client):
    faker = Faker('en')
    user_list = []
    number_of_users = 300
    with client.application.app_context():

        for i in range(number_of_users):
            user = User()
            user.name = faker.name()
            user.password = faker.password()
            user.email = faker.email()
            user_list.append(user)

        db.session.add_all(user_list)
        db.session.commit()
    response = client.get("/users")
    assert response.status_code == 200
    assert b"300" in response.data
