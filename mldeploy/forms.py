from flask_wtf import Form
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import SelectField, StringField, TextAreaField
from wtforms.validators import DataRequired

from .domain import TrainingLibrariesEnum


class AddModelForm(Form):
    name = StringField('Name', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    training_library = SelectField('Training library', choices=[
        (TrainingLibrariesEnum.SKLEARN, TrainingLibrariesEnum.SKLEARN),
        (TrainingLibrariesEnum.TENSORFLOW, TrainingLibrariesEnum.TENSORFLOW),
    ])
    serialized_model = FileField('Serialized model file', validators=[
        FileRequired(), FileAllowed(['joblib'], 'Joblib extension only!')
    ])
