import os
import unittest

from config import Configuration
from app import app, db
from models import Post, User


class TestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///%s' % os.path.join(Configuration.APP_DIR, 'test.db')
        self.app = app.test_client()
        db.create_all()

    def tear_down(self):
        db.session.remove()
        db.drop_all()

    @classmethod
    def test_create_post(self):
        post = Post(title='Test title1', body='Test body')
        db.session.add(post)
        db.session.commit()
        test_post = Post.query.filter_by(title='Test title').first()
        assert test_post != post

    @classmethod
    def test_register(self):
        user = User(username='test user1', email='test1@test.com', password='test', active=True)
        db.session.add(user)
        db.session.commit()
        test_user = User.query.filter_by(username='test user').first()
        assert test_user != user


if __name__ == '__main__':
    unittest.main()
