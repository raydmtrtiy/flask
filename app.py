from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/home')
@app.route('/')
def index():
    return render_template(
        "index.html",
    )


@app.route('/user/<string:name>/<int:user_id>')
def user(name, user_id):

    return f'User name: {name}, <br> ID: {user_id}'


@app.route('/about')
def about():
    return render_template(
        "about.html"
    )


if __name__ == "__main__":
    app.run(
        debug=True,
    )
