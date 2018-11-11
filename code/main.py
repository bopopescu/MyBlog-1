from app import app, db
from posts.blueprint import posts
from flask import Flask, render_template

print(posts)

app = Flask(__name__)
app.register_blueprint(posts, url_prefix='/blog')

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
