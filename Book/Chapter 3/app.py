from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config["SECRET_KEY"] = "Hard to guess string"

class NameForm(FlaskForm):
    name = StringField("What is your name?", validators=[DataRequired()]) # creates a field for name and ensures it isn't submitted empty.
    submit = SubmitField("Submit")


if __name__=="__main__":
    app.run(debug=True)