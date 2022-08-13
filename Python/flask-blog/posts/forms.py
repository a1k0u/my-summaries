from wtforms import TextAreaField
from wtforms import StringField
from wtforms import Form


class PostEdit(Form):
    title = StringField("Title")
    body = TextAreaField("Content")
