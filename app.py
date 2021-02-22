from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/model/<int:model_id>')
def model_detail():
    pass
