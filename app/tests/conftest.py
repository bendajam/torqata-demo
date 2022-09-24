import pytest
from config import Config
from app import create_app


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    SERVER_NAME = 'localhost:5000'


@pytest.fixture()
def app():
    app = create_app(TestConfig)
    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
