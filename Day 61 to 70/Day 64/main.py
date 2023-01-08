from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators, IntegerField, URLField, DecimalField
from wtforms.validators import DataRequired, input_required, optional
import requests


# TODO: remove the api key before uploading to Git
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

# SQLAlchemy Setup
db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, unique=True, nullable=False)
    review = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(250), unique=True, nullable=False)


with app.app_context():
    db.create_all()


# Setting Up Form:

class ReviewForm(FlaskForm):
    rating = DecimalField(label='Your Rating, between 1.0 to 10.0', places=1,
                          validators=[input_required(), validators.number_range(max=10.0, min=0.0)])
    review = StringField(label='Your Review of the Movie', validators=[optional(), validators.length(max=200)])
    submit = SubmitField('Submit')


class AddMovieForm(FlaskForm):
    title = StringField(label='Movie Title', validators=[input_required(), validators.length(max=50)])
    year = IntegerField(label='Release year', validators=[input_required()])
    description = StringField(label='Movie Description', validators=[optional(), validators.length(max=200)])
    rating = DecimalField(label='Your Rating, between 1.0 to 10.0',
                          validators=[input_required(), validators.number_range(max=10.0, min=0.0)])
    ranking = IntegerField(label='Your Ranking For this Movie.', validators=[optional()])
    review = StringField(label="Your Review For this Movie.", validators=[optional(), validators.length(max=200)])
    img_url = URLField(label='Image Url for the Movie Card.',
                       validators=[optional(), validators.length(max=200), validators.url()])
    submit = SubmitField('Submit')


@app.route("/")
def home():
    with app.app_context():
        # print(db.session.query(Movies).all())
        all_movies = Movies.query.order_by(Movies.rating).all()
        for i in range(len(all_movies)):
            all_movies[i].ranking = len(all_movies) - i
        db.session.commit()
        return render_template("index.html", movies=db.session.query(Movies).all())


@app.route('/delete/<movie_id>')
def delete_movie(movie_id):
    with app.app_context():
        movie = Movies.query.get(movie_id)
        db.session.delete(movie)
        db.session.commit()
        print('Movie Deleted.')
        return redirect('/')


@app.route('/edit/<movie_id>', methods=['GET', 'POST'])
def edit_movie(movie_id):
    form = ReviewForm()
    if form.validate_on_submit():
        movie = Movies.query.get(movie_id)
        movie.review = form.review.data
        movie.rating = form.rating.data
        db.session.commit()
        print('Movie review Updated.')
        return redirect('/')

    if request.method == 'GET':
        with app.app_context():
            return render_template('edit.html', form=ReviewForm(), movie=Movies.query.get(movie_id))


@app.route('/add', methods=['GET', 'POST'])
def add_movie():
    form = AddMovieForm()
    if form.validate_on_submit():
        movie = Movies(title=form.title.data,
                       year=form.year.data,
                       description=form.description.data,
                       rating=form.rating.data,
                       ranking=form.ranking.data,
                       review=form.review.data,
                       img_url=form.img_url.data)
        with app.app_context():
            db.session.add(movie)
            db.session.commit()
            print('added a new movie')
            return redirect('/')
    return render_template('add.html', form=AddMovieForm())


if __name__ == '__main__':
    app.run(debug=True)


# endpoint = 'https://api.themoviedb.org/3/search/movie/'
# json = {
#     'query': 'matrix',
#     'include_adult': True,
#     # 'year': 2022
# }
# header = {'api_key': '',
#           'Content-Type': 'application/json',
#           'charset': 'utf-8'}
#
# backdata = requests.get(endpoint, json=json, headers=header)
# print(backdata.text)
