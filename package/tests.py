from package import app,db,routes
import os
import tempfile
import pytest


@pytest.fixture
def client():
    db_fd, db_path = tempfile.mkstemp()
    appy = app({'TESTING': True, 'DATABASE': db_path})

    with appy.test_client() as client:
        with appy.app_context():
            db()
        yield client

    os.close(db_fd)
    os.unlink(db_path)

def test_empty_db(client):
    """Start with a blank database."""
    rv = client.get('/')
    assert b'No entries here so far' in rv.data
