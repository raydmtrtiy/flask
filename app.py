from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///block.db"
db.init_app(app)
app.app_context().push()



db.create_all()



class Article(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    intro = db.Column(db.String(300), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow())

    def __repr__(self):
        return f'Article{self.id}'


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
