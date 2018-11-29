from flask import Blueprint, render_template, request, redirect, url_for
from models import Post, Tag, User
from .forms import PostForm, RegisterForm, ContactForm
from app import db

from flask_security import login_required

posts = Blueprint('posts', __name__, template_folder='templates')


# page 'Create post'
@posts.route('/create', methods=['POST', 'GET'])
@login_required
def create_post():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']

        try:
            post = Post(title=title, body=body)
            db.session.add(post)
            db.session.commit()
        except:
            print('Something goes wrong')

        return redirect(url_for('posts.index'))

    form = PostForm()
    return render_template('posts/create_post.html', form=form)


# page 'Registration'
@posts.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        try:
            user = User(username=username, email=email, password=password, active=True)
            db.session.add(user)
            db.session.commit()
        except:
            print('Something goes wrong')

        return redirect(url_for('posts.index'))

    form = RegisterForm()
    return render_template('posts/register.html', form=form)


# page 'Edit post'
@posts.route('/<slug>/edit/', methods=['POST', 'GET'])
@login_required
def edit_post(slug):
    post = db.session.query(Post).filter(Post.slug == slug).first_or_404()

    if request.method == 'POST':
        form = PostForm(formdata=request.form, obj=post)
        form.populate_obj(post)
        db.session.commit()

        return redirect(url_for('posts.post_detail', slug=post.slug))

    form = PostForm(obj=post)
    return render_template('posts/edit_post.html', post=post, form=form)


# page 'See all posts'
@posts.route('/')
def index():
    q = request.args.get('q')
    page = request.args.get('page')
    if page and page.isdigit():
        page = int(page)
    else:
        page = 1
    if q:
        posts = Post.query.filter(Post.title.contains(q) | Post.body.contains(q))
    else:
        posts = Post.query.order_by(Post.date.desc())
    pages = posts.paginate(page=page, per_page=5)
    return render_template('posts/index.html', posts=posts, pages=pages)


# page 'Title, tags and body of Post'
@posts.route('/<slug>')
def post_detail(slug):
    post = Post.query.filter(Post.slug == slug).first_or_404()
    tags = post.tags
    return render_template('posts/post_detail.html', post=post, tags=tags)


# page 'posts' title in Tags'
@posts.route('/tag/<slug>')
def tag_detail(slug):
    tag = Tag.query.filter(Tag.slug == slug).first_or_404()
    posts = tag.posts.all()
    return render_template('posts/tag_detail.html', posts=posts, tag=tag)


# page 'About'
@posts.route('/about', methods=['POST', 'GET'])
def about():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('posts/about.html')


# page 'Contact'
@posts.route('/contact', methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        email = request.form['email']
        body = request.form['body']
        return redirect(url_for('index'))
    form = ContactForm()
    return render_template('posts/contact.html', form=form)
