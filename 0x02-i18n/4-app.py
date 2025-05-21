#!/usr/bin/env python3
"""
Flask app with manual locale selection via URL parameter
"""

from flask import Flask, render_template, request
from flask_babel import Babel, _


class Config:
    """
    Config class for app settings
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    Determine the best match language for the user

    Priority:
    1. locale from URL parameters if supported
    2. browser settings
    """
    requested_locale = request.args.get('locale')

    if requested_locale and requested_locale in app.config['LANGUAGES']:
        return requested_locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    Handle the root route
    Returns the rendered translated template
    """
    return render_template('3-index.html')  # Reusing the translated template

