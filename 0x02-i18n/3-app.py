#!/usr/bin/env python3
"""
Flask app with Babel and template translation
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
    Select the best match language from the request
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    Handle the root route
    Returns the rendered 3-index.html template
    """
    return render_template('3-index.html')

