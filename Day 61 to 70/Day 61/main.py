from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from flask_bootstrap import Bootstrap


def create_app():
    application = Flask(__name__)
    Bootstrap(application)
    return application


class LoginForm(FlaskForm):
    email = StringField(label='Email')
    password = PasswordField(label='Password')
    submit = SubmitField(label="Log In")


app = create_app()
app.secret_key = "any-string-you-want-just-keep-it-secret"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
