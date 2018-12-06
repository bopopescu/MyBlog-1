from wtforms import Form, StringField, TextAreaField, PasswordField


class PostForm(Form):
    title = StringField('Title')
    body = TextAreaField('Body')


class RegisterForm(Form):
    username = StringField('Username')
    email = StringField('Email')
    password = PasswordField('Password')


class ContactForm(Form):
    email = StringField('email')
    body = TextAreaField('body')
