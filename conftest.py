import pytest
from app import app

@pytest.fixture
def api():
    client = app.test_client()
    return client