from flask import Flask, render_template, jsonify, request, redirect, url_for

from mldeploy.forms import AddModelForm


app = Flask(__name__)
app.config.update(dict(
    SECRET_KEY="powerful secretkey",
    WTF_CSRF_SECRET_KEY="a csrf secret key"
))


@app.route('/', methods=('GET',))
def dashboard():
    return render_template('dashboard.html')


@app.route('/model', methods=('GET', 'POST'))
def add_model():

    form = AddModelForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('add_model.html', form=form)


@app.route('/model/<int:model_id>')
def model_detail(model_id, methods=('GET',)):
    return render_template('model_detail.html')


@app.route('/model/<int:model_id>/predict', methods=('POST',))
def predict(model_id):
    return jsonify({}, 201)
