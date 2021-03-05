from flask_wtf import Form
from flask_wtf.file import FileField
from wtforms import SelectField, StringField, TextAreaField
from wtforms.validators import DataRequired, regexp


class AddModelForm(Form):
    name = StringField('Name', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    training_library = SelectField('Training library', choices=[('scikit-learn', 'scikit-learn'), ('tensorflow', 'tensorflow')])
    serialized_model = FileField('Serialized model file', validators=[DataRequired(), regexp(r'^[^/\\]\.joblib$')])
