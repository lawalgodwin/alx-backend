#!/usr/bin/env python3
"""A basic Barbel setup"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Basic Barbel configuration"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)

app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locale():
    """determine the best match with our supported languages"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def Home():
    """return home page"""
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run()
