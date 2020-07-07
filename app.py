from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from os import environ

# ip address 82.16.221.36
# 211c8c0e484b5eec9d582727aefbf64e

app = Flask(__name__)

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


class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    f_name = db.Column(db.String(30), nullable=False)
    l_name = db.Column(db.String(30), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(300), nullable=False, unique=True)

    def __repr__(self):
        return ''.join(
            [
                'Title: ' + self.title + '\n'
                                         'Name: ' + self.f_name, + ' ' + self.l_name + '\n'
                                                                                       'Content: ' + self.content
            ]
        )


@app.route('/')
@app.route('/home')
def home():
    post_data = Posts.query.all()
    return render_template('homepage.html', title='Homepage', posts=post_data)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/create')
def create():
    db.create_all()
    post = Posts(f_name='Hulk', l_name='Hogan', title='Mr', content='Some content')
    post2 = Posts(f_name='Steve', l_name='Austin', title='Mr', content='Some more content')
    db.session.add(post)
    db.session.add(post2)
    db.session.commit()
    return "Added the table and populated it with some records"


@app.route('/delete')
def delete():
    #db.drop_all()
    db.session.query(Posts).delete()
    db.session.commit()
    return "Everything is gone"


if __name__ == '__main__':
    app.run()
