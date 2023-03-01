from flask import Flask, request, make_response, redirect, abort

app = Flask(__name__)

@app.route('/')
def index():
    user_agent = request.headers.get("User-Agent")
    return f"<p> Your browser is {user_agent[:7]}. </p>"

def lol():
    return "This is the troll page."

# Adding a url:
app.add_url_rule('/lol', 'troll', lol)

# Adding a dynamic username section:
@app.route("/<name>")
def user(name):
    return f"<h1> Hello {name}! <h1>"

print(app.url_map)

@app.route("/restricted")
def restricted():
    response = make_response("<h1> The document is restricted </h1>")
    response.set_cookie('answer', '42')
    return response

if __name__ == "__main__":
    # The debug=True allows us to reload and see errors.
    app.run(debug=True)


# There are some more like redirects and aborts, which just change or interrupt the webpage, if a criteria isn't met.