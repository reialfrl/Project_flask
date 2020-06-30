from wtforms import Form, HiddenField
from wtforms import validators 
from wtforms import StringField, PasswordField, BooleanField, TextAreaField
from wtforms.fields.html5 import EmailField

from .models import User

def length_honeypot(form, field):
    #Function to prevent attacks csrf honeypots
    if len(field.data) > 0:
        raise validators.ValidationError('Only human can completed this task!')

def root_validator(form, field):
    # simple restriction
    if field.data == 'root' or field.data == 'Root':
        raise validators.ValidationError('Root username is prohibited')

class LoginForm(Form):
    #Class to the login form structure
    username = StringField('Username', [
        validators.length(min=4, max=50, message='The username is out of range.'), 
            validators.Required(message='The username is required')
    ])
    password = PasswordField('Password', [
        validators.length(min=6, max=50, message='The password most have a length between 6 to 50 elements.'), 
        validators.Required(message='The password is required')
    ])

class RegisterForm(Form):
    #Class to the register form structure
    username = StringField('Username', [
        validators.length(min=4, max=50, message='The username is out of range.'),
        validators.Required(message='The username is required.'),
        root_validator
    ])
    email = EmailField('Email', [
        validators.length(min=6, max=100), 
        validators.Email(message='The email is invalid.'),
        validators.Required(message='The email is required.')
    ])
    password = PasswordField('Password', [
        validators.length(min=6, max=50, message='The password most have a length between 6 to 50 elements.'),
        validators.EqualTo('confirm_password', message='The password is not equal.'),
        validators.Required(message='The email is required.')
    ])
    confirm_password = PasswordField('Confirm password')
    accept = BooleanField('', [
        validators.DataRequired()
    ])
    honeypot = HiddenField("", [length_honeypot])

    def validate_username(self, username):
        if User.get_by_username(username.data):
            raise validators.ValidationError('Username already exist')

    def validate_email(self, email):
        if User.get_by_email(email.data):
            raise validators.ValidationError('Email already exist')

    def validate(self):
        if not Form.validate(self):
            return False

        if len(self.password.data) < 3:
            self.password.errors.append('The password is very short')   
            return False         

        return True            

class TaskForm(Form):
    #Class to the task form structure
    title = StringField('Title', [
        validators.length(min=4, max=50, message='Title is out of range.'), 
        validators.DataRequired(message='Title is required.')
    ])
    description = TextAreaField('Description', [
        validators.DataRequired(message='Description is required.')
    ], render_kw={'rows': 5})