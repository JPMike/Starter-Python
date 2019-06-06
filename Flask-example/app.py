from flask import Flask, url_for, request, render_template, make_response, session, redirect
from werkzeug.utils import secure_filename

app = Flask(__name__)

app.secret_key = b'\xa7\xfd\x04l)\xd6Ef\x82\xca\xfb\xe3NOl\x01'


@app.route("/")
def index():
    username = request.cookies.get('username', "default")
    print(username)
    resp = make_response(render_template("index.html"))
    resp.set_cookie("username", username)
    return resp


@app.route("/hello/")
@app.route("/hello/<name>")
def hello(name=None):
    return render_template("hello.html", name=name)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session["username"] = request.form["username"]
        if valid_login(request.form["username"],
                       request.form["password"]):
            return log_the_user_in(request.form["username"])
        else:
            return redirect(url_for("index"))
    else:
        return """
            <form method="post">
                <p><input type=text name=username>
                <p><input type=text name=password>
                <p><input type=submit value=Login>
            </form>
        """


@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("index"))


def valid_login(username, password):
    print("{}:{}".format(username, password))
    return True


def log_the_user_in(username):
    return "{} login".format(username)


@app.route("/upload", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        f = request.files["the_file"]
        f.save("/var/www/uploads" + secure_filename(f.filename))


@app.route("/user/<username>")
def profile(username):
    return "{}\'s profile".format(username)


@app.route("/post/<int:post_id>")
def show_post(post_id):
    return "Post %d" % post_id


@app.route("/path/<path:subpath>")
def show_subpath(subpath):
    return "Subpath %s" % subpath


@app.route("/projects/")
def projects():
    return "The project page"


@app.route("/about")
def about():
    return "The about page"


@app.errorhandler(404)
def not_found(error):
    print(error)
    resp = make_response(render_template('error.html'), 404)
    return resp


with app.test_request_context():
    print(url_for("index"))
    print(url_for("login"))
    print(url_for("login", next="/"))
    print(url_for("profile", username="John Doe"))
    print(url_for("static", filename="style.css"))

with app.test_request_context("/hello", method="GET"):
    assert request.path == "/hello"
    assert request.method == "GET"
