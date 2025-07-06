from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests, json

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''


BASE_URL = "https://api.themoviedb.org/3/search/movie"
BASE_URL_SINGLE = 'https://api.themoviedb.org/3'

app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movie-collection.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
bootstrap = Bootstrap5(app)




def movie_details(movie_id):
    # movie_id = request.form.get('movie_id') 
    url = f"{BASE_URL_SINGLE}/movie/{movie_id}"
    params = {"api_key": API_KEY}

    response = requests.get(url, params=params)
    data = response.json()
    return data

def get_related_movies(movie_id):
    
    params = {
        "api_key": API_KEY,
        "query": movie_id
    }
    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()
    return response.json().get('results', [])



#------------
class MovieForm(FlaskForm):
    rating = StringField("Your Rating Out of 10 e.g. 7.5")
    review = StringField("Your Review")
    submit = SubmitField("Done")


#-------Add Movie ----
class AddMovieForm(FlaskForm):
    title = StringField("Movie Title")

    submit = SubmitField("Add Movie")


#----------


# --- Setup DB ---
class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
db.init_app(app)


# --- Movie Model ---
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)  # ✅ fixed
    description: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)
    ranking: Mapped[float] = mapped_column(Float, nullable=False)
    review: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)
    movie_id: Mapped[str] = mapped_column(String(250), nullable=False)

    def __repr__(self):
        return f"<Movie {self.title}>"


second_movie ={
    "title":"Avatar The Way of Water",
    "year":2022,
    "description":"Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
    "rating":7.3,
    "ranking":9,
    "review":"I liked the water.",
    "img_url":"https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
}

# --- Insert Function ---
def add_data(data_):
    with app.app_context():
        movie = Movie(**data_)
        db.session.add(movie)
        db.session.commit()
        print(f"Added: {movie}")

# --- Create DB + Insert Record ---
with app.app_context():
    db.create_all() 
    # add_data(second_movie)       # ✅ Create tables

def read_data():
    with app.app_context():
        result = db.session.execute(db.select(Movie).order_by(Movie.title))
        all_books = result.scalars()
        return all_books.all()

@app.context_processor
def inject_bootstrap():
    return dict(bootstrap5=bootstrap)

@app.route("/")
def home():
    data_ = read_data()
    return render_template("index.html", movies= data_)

@app.route("/edit", methods=["GET", "POST"])
def rate_movie():
    form = MovieForm()
    movie_id = request.args.get("id")
    movie = db.get_or_404(Movie, movie_id)
    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", movie=movie, form=form)

@app.route("/delete", methods=["GET", "POST"])
def delete_movie():
    movie_id = request.args.get("id")
    with app.app_context():
        movie_to_delete = db.session.execute(db.select(Movie).where(Movie.id == movie_id)).scalar()
        # or book_to_delete = db.get_or_404(Book, book_id)
        db.session.delete(movie_to_delete)
        db.session.commit()
    return redirect(url_for('home'))


@app.route("/add",  methods=["GET", "POST"])
def add_movie():
    form = AddMovieForm()
    if form.validate_on_submit():
        title = form.title.data
        search_results = get_related_movies(title)
        return render_template("select.html", all_movies=search_results)
       
    return render_template("add.html", form=form)




@app.route("/add_movies", methods=["GET", "POST"])
def add_movies():
    movie_id = request.args.get("id")
    data = movie_details(movie_id)
    movie =  {
    "title": data['original_title'],
    "year":data['release_date'].split('-')[0],
    "description":data['overview'],
    "rating":7.3,
    "ranking":9,
    "review":"I liked the water.",
    "img_url":f"https://image.tmdb.org/t/p/w500/{data['poster_path']}",
    "movie_id:": data['id']
    }


    add_data(movie)
    
    # return redirect(url_for('rate_movie', id=data['id']))
    


if __name__ == '__main__':
    app.run(debug=True)
