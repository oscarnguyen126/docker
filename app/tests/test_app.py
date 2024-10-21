import sys
import os
import pytest

# Add the app directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

@pytest.fixture
def client():
    # Set up the Flask app in testing mode
    app.config['TESTING'] = True

    # Create and yield the Flask test client
    with app.test_client() as client:
        yield client

def test_index(client):
    # Make a GET request to the Flask app's index route
    response = client.get('/')

    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200

    # Get the JSON data returned by the Flask app
    json_data = response.get_json()

    # Assert that the response contains 'PostgreSQL version'
    assert 'PostgreSQL version' in json_data

    # Assert that the value of 'PostgreSQL version' is a string
    assert isinstance(json_data['PostgreSQL version'], list)
