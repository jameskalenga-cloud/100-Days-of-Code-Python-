from flask import Flask, render_template, request, redirect

from flask_wtf import FlaskForm

from wtforms.validators import DataRequired

from wtforms import StringField, PasswordField, SubmitField


app = Flask(__name__)
app.secret_key = 'supersecretkey123'  # Required for CSRF protection

class LoginForm(FlaskForm):
    name = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Location', render_kw={"size": 30})
    open_ = StringField('Open', render_kw={"size": 30})
    closed = StringField('Closed', render_kw={"size": 30})
    coffee= StringField('Coffee', render_kw={"size": 30})
    wifi = StringField('Wifi', render_kw={"size": 30})
    power = StringField('Power', render_kw={"size": 30})
    submit = SubmitField('Login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return 'Logged in!'
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
