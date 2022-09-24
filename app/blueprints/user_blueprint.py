from flask import Blueprint, session, current_app, url_for, redirect

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    google = current_app.oauth.create_client(
        'google')  # create the google oauth client
    redirect_uri = url_for('auth.authorize', _external=True)
    return google.authorize_redirect(redirect_uri)


@auth.route('/authorize')
def authorize():
    google = current_app.oauth.create_client(
        'google')  # create the google oauth client
    # Access token from google (needed to get user info)
    token = google.authorize_access_token()
    # userinfo contains stuff u specificed in the scrope
    resp = google.get('userinfo')
    user_info = resp.json()
    # uses openid endpoint to fetch user info
    user = current_app.oauth.google.userinfo()
    # Here you use the profile/user data that you got and query your database find/register the user
    # and set ur own data in the session not the profile from google
    session['profile'] = user_info
    # make the session permanant so it keeps existing after broweser gets closed
    session.permanent = True
    return redirect('/')


@auth.route('/logout')
def logout():
    for key in list(session.keys()):
        session.pop(key)
    return redirect('/')
