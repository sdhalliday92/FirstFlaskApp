from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
@app.route('/home')
def hello_world():
    return render_template('homepage.html', title='Homepage')


@app.route('/about')
def about():
    return '''
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>About Page</title>
    </head>
    <body>
        <h1>This about page</h1>
    </body>
    </html>
    '''


if __name__ == '__main__':
    app.run()
