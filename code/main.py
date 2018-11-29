from app import app, db
from posts.blueprint import posts
from flask import Flask, render_template


#app = Flask(__name__)
app.register_blueprint(posts, url_prefix='/blog')


@app.route('/')
def index():
    return render_template('index.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run()
