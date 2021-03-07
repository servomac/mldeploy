from flask_wtf import Form
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import SelectField, StringField, TextAreaField
from wtforms.validators import DataRequired


class AddModelForm(Form):
    name = StringField('Name', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    training_library = SelectField('Training library', choices=[
        ('scikit-learn', 'scikit-learn'), ('tensorflow', 'tensorflow')
    ])
    serialized_model = FileField('Serialized model file', validators=[
        FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!')
    ])
