from flask import Flask
from flask import render_template
#from app import app

app = Flask(__name__)

#def home():
#  return "Welcome to my app!"

@app.route("/")
@app.route('/index')
def index():
    user = {'username': 'Roman'}
    posts = [
        {
            'author': {'username': 'Nastia'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
