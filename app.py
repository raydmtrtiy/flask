from datetime import datetime

from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///block.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
app.app_context().push()


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    intro = db.Column(db.String(300), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow())

    def __repr__(self):
        return f'Article{self.id}'


db.create_all()


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


@app.route('/create-article', methods=['POST', 'GET'])
def create_article():
    if request.method == 'POST':
        title = request.form['title']
        intro = request.form['intro']
        text = request.form['text']

        article = Article(title=title, intro=intro, text=text)

        try:
            db.session.add(article)
            db.session.commit()
            return redirect('/posts')
        except:
            return "An error occurred while adding the article"
    else:
        return render_template("create_article.html")


if __name__ == "__main__":
    app.run(
        debug=True,
        use_reloader=False,
    )
