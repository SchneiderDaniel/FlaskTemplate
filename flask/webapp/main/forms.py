from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, SubmitField, TextAreaField, RadioField, DecimalField
from wtforms.validators import DataRequired, Length, Email



class KeywordForm(FlaskForm):
    keyword = StringField('Keyword:', [
        DataRequired()])
    submit = SubmitField('Submit')


