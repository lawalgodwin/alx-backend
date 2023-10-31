#!/usr/bin/env python3
"""A basic Babel setup"""

from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """Basic Barbel configuration"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)

app.config.from_object(Config)

barbel = Babel(app)


@app.route('/', strict_slashes=False)
def Home():
    """return home page"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
