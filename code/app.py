from flask import Flask, redirect, url_for, request
from config import Configuration

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView

from flask_security import SQLAlchemyUserDatastore, Security, current_user
from flask_mail import Mail

app = Flask(__name__)
app.config.from_object(Configuration)
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_TLS=False,
    MAIL_USE_SSL=True,
    MAIL_USERNAME='XXX@gmail.com',
    MAIL_PASSWORD='XXX')
mail = Mail(app)

from models import db

# add migrations to database
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

from models import Post, Tag, User, Role


# for Admin view page
class AdminMixin:
    def is_accessible(self):
        return current_user.has_role('admin')

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('security.login', next=request.url))


# base class for different views
class BaseModelView(ModelView):
    def on_model_change(self, form, model, is_created):
        model.generate_slug()
        return super(BaseModelView, self).on_model_change(form, model, is_created)


class AdminView(AdminMixin, ModelView):
    pass


class HomeAdminView(AdminMixin, AdminIndexView):
    pass


# view of posts for Admin
class PostAdminView(AdminMixin, BaseModelView):
    form_columns = ['title', 'body', 'tags']


# view of tags for Admin
class TagAdminView(AdminMixin, BaseModelView):
    form_columns = ['name', 'posts']


# connect Admin class with admin in app
admin = Admin(app, 'FlaskApp', url='/', index_view=HomeAdminView(name='Home'))
admin.add_view(PostAdminView(Post, db.session))
admin.add_view(TagAdminView(Tag, db.session))


# secure of database
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)
