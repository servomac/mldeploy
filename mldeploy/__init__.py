import os

from flask import Flask

from mldeploy import config


app = Flask(__name__)
app.config.update(dict(
    SECRET_KEY=config.SECRET_KEY,
    WTF_CSRF_SECRET_KEY=config.WTF_CSRF_SECRET_KEY,
))

import mldeploy.views
