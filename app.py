from flask import Flask
from flask import render_template

app = Flask(__name__)

dummyData = [
    {
        "f_name": "Tadas",
        "l_name": "Vaidotas",
        "title": "Mr",
        "content": "Blah blah blah"
    },
    {
        "f_name": "Jim",
        "l_name": "Jones",
        "title": "Mr",
        "content": "More content"
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('homepage.html', title='Homepage', posts=dummyData)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run()
