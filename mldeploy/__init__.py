import os

from flask import Flask, render_template, jsonify, redirect, url_for

import mldeploy.services as services
from mldeploy.forms import AddModelForm
from mldeploy.repositories import InMemoryRepo


app = Flask(__name__)
app.config.update(dict(
    SECRET_KEY="powerful secretkey",
    WTF_CSRF_SECRET_KEY="a csrf secret key"
))

repo = InMemoryRepo()

@app.route('/', methods=('GET',))
def dashboard():
    # call service list models
    model_list = services.list_models(repo)
    return render_template('dashboard.html', models=model_list)


@app.route('/model', methods=('GET', 'POST'))
def add_model():
    form = AddModelForm()
    if form.validate_on_submit():
        data = {
            'name': form.name.data,
            'description': form.description.data,
            'training_library': form.description.data,
            'serialized_model': form.serialized_model.data,
        }
        model = services.create_model(repo, data)
        return redirect(url_for('model_detail', model_id=model.id))
    return render_template('add_model.html', form=form)


@app.route('/model/<int:model_id>')
def model_detail(model_id, methods=('GET',)):
    model = services.get_model_detail(repo, model_id)
    return render_template('model_detail.html', model=model)


@app.route('/model/<int:model_id>/predict', methods=('POST',))
def predict(model_id):
    # call service predict
    return jsonify({}, 201)
