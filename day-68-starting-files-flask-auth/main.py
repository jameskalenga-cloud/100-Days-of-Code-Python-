from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory, session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'

#Login Manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'  # Redirect to login if not logged in




# CREATE DATABASE

class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CREATE TABLE IN DB


class User(UserMixin,db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))


with app.app_context():
    db.create_all()


@app.context_processor
def inject_logged_in():
    return dict(logged_in=current_user.is_authenticated)



# This handles unauthorized access
@login_manager.unauthorized_handler
def unauthorized_callback():
    return render_template("unauthorized.html"), 401


@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))



@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']  # Ideally hash this before storing


        # ✅ Hash and salt the password before storing
        hashed_password = generate_password_hash(
            password,
            method='pbkdf2:sha256',
            salt_length=8
        )

        new_user = User(name=name, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        session['user_name'] = name  # Store the name in session

        login_user(new_user)  # ✅ Log the user in
        return redirect(url_for('secrets'))

    return render_template("register.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = db.session.query(User).filter_by(email=email).first()

        if not user:
            flash("That email does not exist. Please try again or register.")
            return redirect(url_for('login'))

        if not check_password_hash(user.password, password):
            flash("Incorrect password. Please try again.")
            return redirect(url_for('login'))

        login_user(user)
        return redirect(url_for('secrets'))
    
    return render_template("login.html")


@app.route('/secrets')
@login_required
def secrets():
    user_name = session.get('user_name')
    return render_template("secrets.html", user_name= user_name)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
    return send_from_directory(
        directory='static/files',
        path='cheat_sheet.pdf',
        as_attachment=True
    )


if __name__ == "__main__":
    app.run(debug=True)
