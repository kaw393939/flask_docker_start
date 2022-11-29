from faker import Faker

from application.database import User, db


def test_about_route(client, app):
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
    response = client.get("/users/1")
    assert response.status_code == 200
    assert b"Address" in response.data