from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print("Username:", username)
        print("Password:", password)
        return f"Logged in as {username}"
    

if __name__ == "__main__":
    app.run(debug=True)