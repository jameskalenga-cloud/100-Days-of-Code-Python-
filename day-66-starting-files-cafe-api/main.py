from flask import Flask, jsonify, render_template, request, url_for,redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import random


'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random")
def getRandom():
    all_cafes = db.session.execute(db.select(Cafe)).scalars().all()
    if not all_cafes:
        return jsonify(error="No cafes found"), 404
    random_cafe = random.choice(all_cafes)
    
    return jsonify(cafe=random_cafe.to_dict())
    

@app.route("/all")
def get_all_cafes():
    result = db.session.execute(db.select(Cafe)).scalars().all()
    cafes = [cafe.to_dict() for cafe in result]
    return jsonify(cafes=cafes)



@app.route("/search")
def get_cafes_by_location():
    loc = request.args.get("loc", type=str)
    if not loc:
        return jsonify(error="Please provide a 'loc' query parameter"), 400

    cafés = db.session.execute(db.select(Cafe).filter_by(location=loc)).scalars().all()
    if not cafés:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."}), 404
    
    return jsonify(cafes=[c.to_dict() for c in cafés])

def str_to_bool(value):
    return value.lower() == "true"

# HTTP POST - Create Record
@app.route("/add", methods=["GET", "POST"])
def add_items():
    if request.method == "POST":
        new_cafe = Cafe(
        name=request.form["name"],
        map_url=request.form["map_url"],
        img_url = request.form["img_url"],
        location = request.form["location"], 
        seats=request.form["seats"],
        has_toilet=str_to_bool(request.form["has_toilet"]),
        has_wifi=str_to_bool(request.form["has_wifi"]),
        has_sockets=str_to_bool(request.form["has_sockets"]),
        can_take_calls=str_to_bool(request.form["can_take_calls"]),
            # coffee_price=request.form.get("coffee_price")  
        )
        db.session.add(new_cafe)
        db.session.commit()
        return jsonify(response={"success": "Successfully added the new cafe."})



# HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    
    
    if request.method == "PATCH":
        new_price=request.form["new_price"]

        if not new_price:
            return jsonify(error="Missing 'new_price' parameter."), 400

        try:
            cafe = db.get_or_404(Cafe, cafe_id)
            cafe.coffee_price = new_price
            db.session.commit()
            return jsonify(success=f"Coffee price updated to {new_price} for cafe ID {cafe_id}"), 200

        except AttributeError:
            return jsonify(error="Cafe not found."), 404



# HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
