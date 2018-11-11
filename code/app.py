from flask import Flask, render_template
from config import Configuration
from flask_sqlalchemy import SQLAlchemy

from datetime import datetime
import re

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

app = Flask(__name__)
app.config.from_object(Configuration)

db = SQLAlchemy(app)


migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


#def slugify(s):
#    pattern = r'[^\w+]'
#    return re.sub(pattern, '-', s)


#post_tags = db.Table('post_tags',
#                    db.Column('post_id', db.Integer, db.ForeignKey('post.id')),
#                    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'))
#    )


#class Post(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    title = db.Column(db.String(140))
#    slug = db.Column(db.String(140), unique=True)
#    body = db.Column(db.Text)
#    date = db.Column(db.DateTime, default=datetime.now())
#    tags = db.relationship('Tag', secondary=post_tags, backref=db.backref('posts', lazy='dynamic'))

#    def __init__(self, *args, **kwargs):
#        super(Post, self).__init__(*args, **kwargs)
#        self.generate_slug()

#    def generate_slug(self):
#        if self.title:
#            self.slug = slugify(self.title)

#    def __repr__(self):
#        return '<Post id: {}, title: {}>'.format(self.id, self.title)


#class Tag(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    name = db.Column(db.String(100))
#    slug = db.Column(db.String(100))

#    def __init__(self, *args, **kwargs):
#        super(Tag, self).__init__(*args, **kwargs)
#        self.slug = slugify(self.name)

#    def __repr__(self):
#        return '<Tag id: {}, name: {}>'.format(self.id, self.name)


@app.route('/')
def index():
    return render_template('index.html')


#@app.route('/posts')
#def posts():
#    posts = Post.query.all()
#    return render_template('posts.html', posts=posts)


#@app.route('/<slug>')
#def post_detail(slug):
#    post = Post.query.filter(Post.slug == slug).first()
#    return render_template('post_detail.html', post=post)
