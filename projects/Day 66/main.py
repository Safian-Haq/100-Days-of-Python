from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


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
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/random', methods=['GET'])
def get_random_cafe():
    all_cafe_ids = db.session.query(Cafe.id).all()
    random_cafe = Cafe.query.get(random.choice(all_cafe_ids))
    # I wrote this monstrosity ... :/
    # return jsonify(
    #     {
    #         'cafe': {
    #             'can_take_calls': random_cafe.can_take_calls,
    #             'coffee_price': random_cafe.coffee_price,
    #             'has_sockets': random_cafe.has_sockets,
    #             'has_toilet': random_cafe.has_toilet,
    #             'has_wifi': random_cafe.has_wifi,
    #             'id': random_cafe.id,
    #             'img_url': random_cafe.img_url,
    #             'location': random_cafe.location,
    #             'map_url': random_cafe.map_url,
    #             'name': random_cafe.name,
    #             'seats': random_cafe.seats
    #         }
    #     }
    # )
    # A simpler and dynamic way
    return jsonify(cafe=random_cafe.to_dict())


@app.route('/all', methods=['GET'])
def get_all():
    all_cafes = db.session.query(Cafe).all()
    return jsonify(cafe=[cafe.to_dict() for cafe in all_cafes])


@app.route('/search', methods=['GET'])
def search():
    target_cafes = db.session.query(Cafe).filter(Cafe.location == request.args['loc'])
    target_cafes = jsonify(cafes=[cafe.to_dict() for cafe in target_cafes])
    if target_cafes.json['cafes']:
        return target_cafes
    else:
        return jsonify(error={'Not Found': "Sorry, we don't have a cafe at the specified location."})


@app.route('/add', methods=['POST'])
def add():
    try:
        new_cafe = Cafe(
            name=request.form.get("name"),
            map_url=request.form.get("map_url"),
            img_url=request.form.get("img_url"),
            location=request.form.get("loc"),
            has_sockets=bool(request.form.get("sockets")),
            has_toilet=bool(request.form.get("toilet")),
            has_wifi=bool(request.form.get("wifi")),
            can_take_calls=bool(request.form.get("calls")),
            seats=request.form.get("seats"),
            coffee_price=request.form.get("coffee_price"),
        )
        db.session.add(new_cafe)
        db.session.commit()
        return jsonify(response={'success': 'Successfully add the new cafe.'})
    except KeyError:
        return jsonify(response={'error': 'KeyError - Please recheck your parameters.'})


@app.route('/update-price', methods=['PATCH'])
def update_price():
    target_cafe = db.session.query(Cafe).filter(Cafe.id == request.args['cafe_id']).first()
    if target_cafe == None:
        return jsonify(error={'Not Found': "'cafe_id' not found in database."}), 404

    target_cafe.coffee_price = request.args['coffee_price']
    db.session.commit()

    return jsonify(response={'success': 'Successfully updated the price.'}), 200


@app.route('/delete', methods=['DELETE'])
def delete_cafe():
    if request.args['api_key'] in ['API_KEY']:
        Cafe.query.filter_by(id=request.args['cafe_id']).delete()
        db.session.commit()
        return jsonify(response={'success': 'Successfully deleted the specified cafe.'}), 200
    else:
        return jsonify(error={'Access Denied': "Invalid api key."}), 403


if __name__ == '__main__':
    app.run(debug=True)
