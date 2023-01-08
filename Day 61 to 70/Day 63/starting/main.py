from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# import sqlite3
app = Flask(__name__)

db = SQLAlchemy()
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


# CREATE TABLE
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'


# with app.app_context():
#     db.create_all()
#
#     # CREATE RECORD
#     new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)
#     db.session.add(new_book)
#     db.session.commit()

all_books = []


@app.route('/')
def home():
    return render_template('index.html', books=db.session.query(Book).all())


@app.route("/add", methods=["GET"])
def add():
    return render_template('add.html')


@app.route("/show", methods=["POST"])
def show():
    with app.app_context():
        db.session.add(
            Book(title=request.form.get('title'),
                 author=request.form.get('author'),
                 rating=request.form.get('rating'))
        )
        db.session.commit()
        print('data added')
        return redirect('/')


@app.route('/update_rating/<book_id>', methods=['GET', 'POST'])
def update_rating(book_id):
    if request.method == 'GET':
        return render_template('edit_rating.html',
                               book=Book.query.filter_by(id=book_id).first())

    if request.method == "POST":
        book = Book.query.get(book_id)
        book.rating = request.form.get('rating')
        db.session.commit()
        print(f'Rating Updated of Book {book_id}')
        return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
