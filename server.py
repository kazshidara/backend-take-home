from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/json')
def api_call():
    return render_template('index.html')


@app.route('/show_posts')
def show_user_posts():
    return render_template('index.html')