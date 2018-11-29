from app import app
from posts.blueprint import posts
from flask import render_template

# connect blueprints
app.register_blueprint(posts, url_prefix='/blog')


# show Home page
@app.route('/')
def index():
    return render_template('index.html')


# show error page
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


# run application
if __name__ == '__main__':
    app.run()
