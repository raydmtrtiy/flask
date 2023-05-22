from flask import Flask

app = Flask(__name__)


@app.route('/home')
@app.route('/')
def index():
    return "Hello World"


@app.route('/user/<string:name>/<int:user_id>')
def user(name, user_id):

    return f'User name: {name}, <br> ID: {user_id}'


@app.route('/about')
def about():
    return "About World"


if __name__ == "__main__":
    app.run(
        debug=True,
    )
