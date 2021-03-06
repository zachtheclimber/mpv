import pytest


def test_index(app: pytest.fixture) -> None:
    """Assert that a status code of 200 is returned from /"""
    with app.test_client() as client:
        index = client.get('/')
        assert index.status == '200 OK'
