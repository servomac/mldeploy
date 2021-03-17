import os

from flask import Flask

import mldeploy.db as db
from mldeploy import config


app = Flask(__name__)
app.config.update(dict(
    SECRET_KEY=config.SECRET_KEY,
    WTF_CSRF_SECRET_KEY=config.WTF_CSRF_SECRET_KEY,
))
app.session = db.db_session

@app.teardown_appcontext
def shutdown_session(exception=None):
    db.db_session.remove()

db.init_app(app)

import mldeploy.views
