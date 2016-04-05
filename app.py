from flask import Flask, render_template, request, make_response, redirect


app = Flask(__name__)


@app.route('/')
def index():
    if 'username' in request.cookies:
        return render_template('user.html',
                               name=request.cookies.get('username'))
    else:
        return render_template('index.html')


@app.route('/login/', methods=['POST'])
def login():
    if request.form['password'] == '123':
        response = make_response(redirect('/'))
        response.set_cookie('username', request.form['username'])
        return response


@app.route('/user/<username>')
def get_user(username):
    return render_template('user.html', name=username)


if __name__ == '__main__':
    app.run()
