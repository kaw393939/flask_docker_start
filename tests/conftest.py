import pytest

from application import init_app as create_app
from application.database import db


@pytest.fixture(scope="function")
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })

    # other setup can go here
    with app.app_context():
        db.session.remove()
        db.drop_all()
        db.create_all()
        yield app

        db.session.remove()
        # Uncomment To Reset Database After Test
        # db.drop_all()

    # clean up / reset resources here


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()


@pytest.fixture(scope="function")
def app_clean_db():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })

    # other setup can go here
    with app.app_context():
        db.session.remove()
        db.drop_all()
        yield app
        db.session.remove()
