from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Name: <input type="text" />'


@app.route('/user/<username>')
def get_user(username):
    return render_template('user.html', name=username)


if __name__ == '__main__':
    app.run()
