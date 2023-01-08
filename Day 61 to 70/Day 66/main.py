import random

from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
db.init_app(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        # Method 1.
        dictionary = {}
        # Loop through each column in the data record
        for column in self.__table__.columns:
            # Create a new dictionary entry;
            # where the key is the name of the column
            # and the value is the value of the column
            dictionary[column.name] = getattr(self, column.name)
        return dictionary

        # Method 2. Altenatively use Dictionary Comprehension to do the same thing.
        # return {column.name: getattr(self, column.name) for column in self.__table__.columns}


with app.app_context():
    db.create_all()


@app.route("/random")
def get_random_cafe():
    # cafes = db.session.query(Cafe).all()
    # print(len(cafes))
    cafes = Cafe.query.all()
    # print(cafes)
    random_cafe = random.choice(cafes)
    # Simply convert the random_cafe data record to a dictionary of key-value pairs.
    return jsonify(cafe=random_cafe.to_dict())


@app.route('/all')
def all_cafes():
    cafes = Cafe.query.all()
    cafe_dat = [cafe.to_dict() for cafe in cafes]
    return jsonify(cafes=cafe_dat)


@app.route('/search')
def search_cafe_at_location():
    query_location = request.args.get('loc')
    cafe = db.session.query(Cafe).filter_by(location=query_location).first()
    if cafe:
        return jsonify(cafe=cafe.to_dict())
    else:
        return jsonify(error={'code': 404, 'error-message': 'No cafe found on that location'})


@app.route('/add', methods=['POST'])
def add_cafe():
    cafe = Cafe(name=request.form.get('name'),
                map_url=request.form.get('map_url'),
                img_url=request.form.get('img_url'),
                location=request.form.get('location'),
                seats=request.form.get('seats'),
                has_toilet=bool(request.form.get('has_toilet')),
                has_wifi=bool(request.form.get('has_wifi')),
                has_sockets=bool(request.form.get('has_sockets')),
                can_take_calls=bool(request.form.get('can_take_calls')),
                coffee_price=str(request.form.get('coffee_price')))
    with app.app_context():
        db.session.add(cafe)
        db.session.commit()
        return "cafe added"


@app.route('/update-price/<int:cafe_id>', methods=["PATCH"])
def update_price(cafe_id):
    cafe = db.session.query(Cafe).get(cafe_id)
    if cafe:
        cafe.coffee_price = str(request.form.get('coffee_price'))
        with app.app_context():
            db.session.commit()
            return f"Price updated for Cafe {cafe_id}, with {request.form.get('coffee_price')}"
    else:
        return jsonify(error={'code': 404, "Message": 'The Cafe does not Exist'})


@app.route('/report-closed/<int:cafe_id>', methods=["DELETE"])
def delete(cafe_id):
    cafe = db.session.query(Cafe).get(cafe_id)
    if cafe:
        if request.args.get('api_key') == 'badenforcer':
            with app.app_context():
                db.session.delete(cafe)
                db.session.commit()
                return jsonify(response={"success": "Successfully Removed cafe Entry."}), 200
        else:
            return jsonify(error={"Not Authorized": "Invalid API KEY"}), 403
    else:
        # 404 = Resource not found
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404


#TODO: delete function shows error for session and stuff, need to be fixed later. but all other things work



## HTTP POST - Create Record

## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
