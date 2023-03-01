from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

def user(name):
    return render_template("user.html", name=name)

app.add_url_rule('/<name>', "name", user)

if __name__ == "__main__":
    app.run(debug=True)