#!/usr/bin/env python3
"""A basic Barbel setup"""

from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Union, Dict

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    """Return a user if exists or None"""
    user_id = request.args.get("login_as", None)
    if not user_id:
        return None
    return users.get(int(user_id), None)


class Config:
    """Basic Barbel configuration"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)

app.config.from_object(Config)

babel = Babel(app)


@app.before_request
def before_request():
    """Execute this before all other functions"""
    g.user = get_user()


@babel.localeselector
def get_locale():
    """determine the best match with our supported languages"""
    locale_in_url = locale = request.args.get('locale')
    locale_in_user_settings = g.user.get('locale') if g.user else None
    locale_in_headers = request.headers.get('locale')
    locale = locale_in_url or locale_in_user_settings or locale_in_headers
    if locale and (locale in app.config['LANGUAGES']):
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def Home():
    """return home page"""
    return render_template('6-index.html')


if __name__ == '__main__':
    app.run()
