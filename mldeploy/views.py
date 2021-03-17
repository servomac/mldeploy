from flask import render_template, jsonify, redirect, request, url_for

import mldeploy.services as services
from mldeploy.forms import AddModelForm
from mldeploy.repositories import SqlAlchemyModelRepo

from mldeploy import app


@app.route('/', methods=('GET',))
def dashboard():
    repo = SqlAlchemyModelRepo(app.session)
    model_list = services.list_models(repo)
    return render_template('dashboard.html', models=model_list)


@app.route('/model', methods=('GET', 'POST'))
def add_model():
    form = AddModelForm()
    if form.validate_on_submit():
        data = {
            'name': form.name.data,
            'description': form.description.data,
            'training_library': form.training_library.data,
            'serialized_model': form.serialized_model.data,
        }
        repo = SqlAlchemyModelRepo(app.session)
        model = services.create_model(repo, data)
        return redirect(url_for('model_detail', model_id=model.id))
    return render_template('add_model.html', form=form)


@app.route('/model/<int:model_id>', methods=('GET',))
def model_detail(model_id):
    repo = SqlAlchemyModelRepo(app.session)
    model = services.get_model_detail(repo, model_id)
    return render_template('model_detail.html', model=model)


@app.route('/model/<int:model_id>/predict', methods=('POST',))
def predict(model_id):
    json_data = request.get_json()
    repo = SqlAlchemyModelRepo(app.session)
    prediction = services.predict(repo, model_id, json_data.get('input'))
    return jsonify(prediction), 201
