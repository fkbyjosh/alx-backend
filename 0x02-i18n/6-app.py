#!/usr/bin/env python3
"""
Flask app that uses user-defined locale settings
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, _


class Config:
    """
    Config class for i18n settings
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},  # Invalid locale
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


def get_user():
    """
    Returns user dict if login_as is valid and exists, else None
    """
    try:
        user_id = int(request.args.get("login_as"))
        return users.get(user_id)
    except (TypeError, ValueError):
        return None


@app.before_request
def before_request():
    """
    Runs before each request to store user in global g
    """
    g.user = get_user()


@babel.localeselector
def get_locale():
    """
    Select best language based on:
    1. URL param
    2. user locale
    3. request header
    4. default
    """
    # 1. From URL query param
    url_locale = request.args.get('locale')
    if url_locale in app.config['LANGUAGES']:
        return url_locale

    # 2. From user preferences (if logged in)
    if g.get('user'):
        user_locale = g.user.get('locale')
        if user_locale in app.config['LANGUAGES']:
            return user_locale

    # 3. From Accept-Language header
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    Render main page with localized content
    """
    return render_template('6-index.html')

