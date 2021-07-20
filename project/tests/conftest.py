import pytest
from ..app import app, db
from ..sample_data import populate_data_to_db


@pytest.fixture()
def test_app():
    """"fixture to get flask app test instance connected to test database"""
    print('fixture test app')
    app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:///tests/test.db'
    app.config['TESTING'] = True
    return app


@pytest.fixture()
def client(test_app):
    """fixture to populate test.db with 2 entries and get test app's test_client"""
    print('fixture test client')
    populate_data_to_db(db, 2)
    return test_app.test_client()


@pytest.fixture()
def logged_client(client):
    """fixture to add user to current session"""
    with client.session_transaction() as sess:
        sess['user'] = 'some_user'
    return client
