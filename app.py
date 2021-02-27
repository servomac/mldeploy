from flask import Flask, render_template, jsonify, request, redirect, url_for, flash

app = Flask(__name__)


@app.route('/', methods=('GET',))
def dashboard():
    return render_template('dashboard.html')


@app.route('/model', methods=('GET', 'POST'))
def add_model():
    if request.method == 'POST':
        name = request.form.get('name')
        error = None

        if not name:
            error = 'Name is required.'

        if error is None:
            # insert into db
            return redirect(url_for('model_detail'))

        flash(error)

    return render_template('add_model.html')


@app.route('/model/<int:model_id>')
def model_detail(model_id, methods=('GET',)):
    return render_template('model_detail.html')


@app.route('/model/<int:model_id>/predict', methods=('POST',))
def predict(model_id):
    return jsonify({}, 201)
