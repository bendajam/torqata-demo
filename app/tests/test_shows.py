from flask import url_for
from http import HTTPStatus

def test_access_shows(client):
  with client.session_transaction() as session:
    session['profile'] = {'email': 'testemail@test.com', 'name': 'Test User'}
  with client.application.app_context():
    response = client.get(url_for("shows.show_list"))
  assert HTTPStatus.OK == response.status_code

def test_unauthorized(client):
  with client.application.app_context():
    response = client.get(url_for("shows.show_list"))

  # currently the unauthorized redirects to login
  assert HTTPStatus.FOUND == response.status_code