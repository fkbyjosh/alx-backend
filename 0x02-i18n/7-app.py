#!/usr/bin/env python3
"""
Flask app that selects locale and timezone from request or user settings
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, _
from pytz import timezone, UnknownTimeZoneError


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
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},  # Invalid
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


def get_user():
    """
    Retrieve user dict if login_as is a valid user ID, else None
    """
    try:
        user_id = int(request.args.get("login_as"))
        return users.get(user_id)
    except (TypeError, ValueError):
        return None


@app.before_request
def before_request():
    """
    Store the user in global g before each request
    """
    g.user = get_user()


@babel.localeselector
def get_locale():
    """
    Determine the best-matching locale
    Priority: URL param > user setting > request headers > default
    """
    url_locale = request.args.get("locale")
    if url_locale in app.config["LANGUAGES"]:
        return url_locale

    if g.user:
        user_locale = g.user.get("locale")
        if user_locale in app.config["LANGUAGES"]:
            return user_locale

    return request.accept_languages.best_match(app.config["LANGUAGES"])


@babel.timezoneselector
def get_timezone():
    """
    Determine the best-matching timezone
    Priority: URL param > user setting > default
    Validate using pytz
    """
    tz_param = request.args.get("timezone")
    try:
        if tz_param:
            return timezone(tz_param).zone
    except UnknownTimeZoneError:
        pass

    if g.user:
        user_tz = g.user.get("timezone")
        try:
            return timezone(user_tz).zone
        except UnknownTimeZoneError:
            pass

    return app.config["BABEL_DEFAULT_TIMEZONE"]


@app.route('/')
def index():
    """
    Render main page
    """
    return render_template('7-index.html')

