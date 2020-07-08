from flask import Flask, redirect, url_for
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from os import environ
from flask_bcrypt import Bcrypt

from forms import RegistrationForm

app = Flask(__name__)
bcrypt = Bcrypt(app)

app.config['SECRET_KEY'] = environ.get('SECRET_KEY')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://' + \
                                        environ.get('MYSQL_USER') + \
                                        ':' + \
                                        environ.get('MYSQL_PASSWORD') + \
                                        '@' + \
                                        environ.get('MYSQL_HOST') + \
                                        ':' + \
                                        environ.get('MYSQL_PORT') + \
                                        '/' + \
                                        environ.get('MYSQL_DB_NAME')

db = SQLAlchemy(app)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(500), nullable=False, unique=True)
    password = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return ''.join(['UserID: ', str(self.id), '\r\n', 'Email: ', self.email])


class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    f_name = db.Column(db.String(30), nullable=False)
    l_name = db.Column(db.String(30), nullable=False)
    title = db.Column(db.String(10), nullable=False)
    content = db.Column(db.String(300), nullable=False, unique=True)

    def __repr__(self):
        return ''.join(
            [
                'Title: ' + self.title + '\n'
                                         'Name: ' + self.f_name, + ' ' + self.l_name + '\n'
                                                                                       'Content: ' + self.content
            ]
        )


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hash_pw = bcrypt.generate_password_hash(form.password.data)

        user = Users(email=form.email.data, password=hash_pw)

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/')
@app.route('/home')
def home():
    post_data = Posts.query.all()
    return render_template('homepage.html', title='Homepage', posts=post_data)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = PostsForm()
    if form.validate_on_submit():
        post_data = Posts(
            f_name=form.f_name.data,
            l_name=form.l_name.data,
            title=form.title.data,
            content=form.content.data
        )
        db.session.add(post_data)
        db.session.commit()
        return redirect(url_for('home'))
    else:
        return render_template('post.html', title='Add a post', form=form)


@app.route('/create')
def create():
    db.drop_all()
    db.create_all()
    db.session.commit()
    return "Database created"


@app.route('/delete')
def delete():
    # db.drop_all()
    db.session.query(Posts).delete()
    db.session.commit()
    return "Everything is gone"


if __name__ == '__main__':
    app.run()
