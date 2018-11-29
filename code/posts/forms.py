from wtforms import Form, StringField, TextAreaField


class PostForm(Form):
    title = StringField('Title')
    body = TextAreaField('Body')


class RegisterForm(Form):
    username = StringField('Username')
    email = StringField('Email')
    password = StringField('Password')


class ContactForm(Form):
    email = StringField('email')
    body = TextAreaField('body')
