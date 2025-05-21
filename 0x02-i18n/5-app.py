#!/usr/bin/env python3
"""
Flask app with user mock login and localized login messages
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, _


class Config:
    """
    Config class for app settings
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


def get_user():
    """
    Returns a user dictionary if login_as is valid, else None
    """
    try:
        user_id = int(request.args.get('login_as'))
        return users.get(user_id)
    except (TypeError, ValueError):
        return None


@app.before_request
def before_request():
    """
    Set g.user to the current logged-in user if any
    """
    g.user = get_user()


@babel.localeselector
def get_locale():
    """
    Determine best match language from:
    1. URL param ?locale=
    2. user preference
    3. Accept-Language header
    """
    url_locale = request.args.get("locale")
    if url_locale in app.config['LANGUAGES']:
        return url_locale

    if g.get('user'):
        user_locale = g.user.get('locale')
        if user_locale in app.config['LANGUAGES']:
            return user_locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    Render the main template
    """
    return render_template('5-index.html')

