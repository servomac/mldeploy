from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired


class AddModelForm(Form):
    name = StringField('name', validators=[DataRequired()])
    description = StringField('description', validators=[DataRequired()])
