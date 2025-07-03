from flask import Flask, render_template, request, redirect, url_for

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
all_books = []

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
# initialize the app with the extension
db.init_app(app)

##CREATE TABLE
class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'
    
# Create table schema in the database. Requires application context.
with app.app_context():
    db.create_all()





def add_data(form_data):
    # CREATE RECORD
    with app.app_context():
        new_book = Book( title=form_data['title'], author=form_data['author'], rating=form_data['rating'])
        db.session.add(new_book)
        db.session.commit()

def read_data():
    with app.app_context():
        result = db.session.execute(db.select(Book).order_by(Book.title))
        all_books = result.scalars()
        return all_books.all()

def read_single(id_):
    with app.app_context():
        book = db.session.execute(db.select(Book).where(Book.id == id_)).scalar()
        return book


def update(book_id, value_):
     
    with app.app_context():
        book_to_update = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
        # or book_to_update = db.get_or_404(Book, book_id)  
        book_to_update.rating = value_
        db.session.commit() 


@app.route('/')
def home():
    all_books = read_data()
    return render_template('index.html',all_books=all_books)



@app.route('/delete')
def delete():
    book_id = request.args.get('id')
    
    with app.app_context():
        book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
        # or book_to_delete = db.get_or_404(Book, book_id)
        db.session.delete(book_to_delete)
        db.session.commit()

    return redirect(url_for('home'))
    
    


@app.route("/add")
def add():
    return render_template('add.html')

@app.route("/edit")
def adit():
    book_id = request.args.get('id')
    data_ = read_single(book_id)
    
    return render_template('edit.html', obj = data_)


@app.route('/update_rating', methods=['POST'])
def update_rating():
    book_id = request.form.get('book_id')
    new_rating = request.form.get('rating')
    
    update(book_id, new_rating)
    
    return redirect('/')


@app.route('/receive_data', methods=['GET', 'POST'])
def receive_data():
    if request.method == 'POST':
        bookauthor = request.form.get('bookauthor')
        bookname = request.form.get('bookname')
        rating = request.form.get('rating')
        form_data = {
            "title": bookname,
            "author": bookauthor,
            "rating": rating,
        }
        add_data(form_data)
        all_books.append(form_data)
        return redirect(url_for('home'))
    return "Use the form to submit book data"


if __name__ == "__main__":
    app.run(debug=True)

