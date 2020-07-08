from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError



def validate_email(email):
    user = Users.query.filter_by(email=email.data).first()

    if user:
        raise ValidationError('Email already in use')


class RegistrationForm(FlaskForm):
    email = StringField('Email',
                        validators=[
                            DataRequired(),
                            Email()
                        ]
                        )
    password = PasswordField('Password',
                             validators=[
                                 DataRequired(),
                             ]
                             )
    confirm_password = PasswordField('Confirm Password',
                                     validators=[
                                         DataRequired(),
                                         EqualTo('password')
                                     ]
                                     )
    submit = SubmitField('Sign Up')


class PostsForm(FlaskForm):
    f_name = StringField(
        'First name',
        validators=[
            DataRequired(),
            Length(min=1, max=30)
        ]
    )

    l_name = StringField(
        'Last name',
        validators=[
            DataRequired(),
            Length(min=1, max=30)
        ]
    )

    title = StringField(
        'Title',
        validators=[
            DataRequired(),
            Length(min=2, max=100)
        ]
    )

    content = StringField(
        'Content',
        validators=[
            DataRequired(),
            Length(min=4, max=300)
        ]
    )

    submit = SubmitField('Make a Post')
