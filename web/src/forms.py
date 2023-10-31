from flask_wtf import FlaskForm
from wtforms import BooleanField, FileField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError

from src.models import User


class RegisterForm(FlaskForm):
    def validate_username(
        self, username_to_check
    ):  # FlaskForm will search for all functions that start with validate_name, then check fields with that name
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError(
                "Username already exists! Please try a different username"
            )

    username = StringField(
        label="User Name:", validators=[Length(min=2, max=30), DataRequired()]
    )
    password1 = PasswordField(
        label="Password:", validators=[Length(min=6), DataRequired()]
    )
    password2 = PasswordField(
        label="Confirm Password:", validators=[EqualTo("password1"), DataRequired()]
    )
    submit = SubmitField(label="Create Account")


class LoginForm(FlaskForm):
    username = StringField(label="User Name:", validators=[DataRequired()])
    password = PasswordField(label="Password:", validators=[DataRequired()])
    submit = SubmitField(label="Sign in")


class SetupForm(FlaskForm):
    company_name = StringField(
        label="Company Name:", default="ACME", validators=[DataRequired()]
    )
    logo = FileField(label="Company Logo:")

    chat_explore = StringField(
        label="Chat Explore Endpoint:",
        default="https://app.akkio.com/project/pd3AI3fUVIaz0QyVXMRd/chat/YB6QBUJgDyvo7B3cJHkn?data=N4IgLglmA2CmIC4QBlYEMAmACAygYwHsAnCAOwHMsARWAWwJABoQALCAZzGIE9EAzNNHaxmABwCuAI2gQ8iMEXEiQGNGDTCwABSKwAbhFgB3eYtgBfIA",
        validators=[DataRequired()],
    )
    dashboard = StringField(
        label="Dashboard Endpoint:",
        default="https://app.akkio.com/dashboard/viewer/RwPGlSOUVs8uRvKkRRJT",
        validators=[DataRequired()],
    )
    insights_report = StringField(
        label="Insights Report Endpoint:",
        default="https://app.akkio.com/project/pd3AI3fUVIaz0QyVXMRd/1/report",
        validators=[DataRequired()],
    )
    submit = SubmitField(label="Submit")
