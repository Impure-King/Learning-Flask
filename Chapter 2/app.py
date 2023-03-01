from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.errorhandler(404)
def error(error):
    return render_template("404.html"), 404

# def user(name):
#     return render_template("user.html", name=name)

# app.add_url_rule('/<name>', "name", user)

@app.route('/control')
def control():
    map = ["nice", "bad"]
    return render_template('control.html', comments = map)

bootstrap = Bootstrap(app)
@app.route('/strap/<name>')
def greet(name):
    return render_template("strap.html", name = name)

if __name__ == "__main__":
    app.run(debug=True)