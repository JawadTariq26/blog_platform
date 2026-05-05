from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField

# WTForm for creating a blog post
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL",default='insert your favoutite image here !', validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


class RegisterForm(FlaskForm):
    name = StringField('Name',validators=[DataRequired()])
    email = EmailField('Email',validators=[DataRequired()])
    password = StringField('Password',validators=[DataRequired()])
    submit = SubmitField('Sign Me UP')

class LoginForm(FlaskForm):
    email = EmailField('Email',validators=[DataRequired()])
    password = StringField('Password',validators=[DataRequired()])
    submit = SubmitField('Login')

class CommentForm(FlaskForm):
    comment = CKEditorField('Comments',validators=[DataRequired()])
    submit = SubmitField('Post Comment')


class InputForm(FlaskForm):
    content = StringField('Type the Topic',validators=[DataRequired()])
    submit = SubmitField('Start Creation')