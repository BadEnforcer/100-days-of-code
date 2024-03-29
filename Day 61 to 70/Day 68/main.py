import flask
from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user, login_manager

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


# Line below only required once, when creating DB.
# db.create_all()

# login


LM = LoginManager(app=app, add_context_processor=True)


@LM.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template("register.html", logged_in=current_user.is_authenticated)

    if request.method == "POST":
        if db.session.query(User).filter_by(email=request.form.get('email')).first():
            flash('Account already exists, Please login.')
            return redirect(url_for('login'))
        else:
            new_user = User(
                email=request.form.get('email'),
                name=request.form.get('name'),
                password=generate_password_hash(password=request.form.get('password'),
                                                salt_length=32,
                                                method='pbkdf2:sha256'))
            # the password is hashed

            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for("secrets"))


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')

        # Find user by email entered.
        user = User.query.filter_by(email=email).first()
        if user:
            # Check stored password hash against entered password hashed.
            if check_password_hash(user.password, password):
                login_user(user)
                return redirect(url_for('secrets'))
        else:
            flash('Account does not exists, Please Register First.')
            return render_template('register.html')

    return render_template("login.html", logged_in=current_user.is_authenticated)


@app.route('/secrets/')
@login_required
def secrets():
    print(current_user.name)
    return render_template("secrets.html", name=current_user.name)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
    return send_from_directory('static', filename="files/cheat_sheet.pdf")


if __name__ == "__main__":
    app.run(debug=True)
