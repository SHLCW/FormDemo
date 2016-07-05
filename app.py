from flask import Flask, render_template, request, make_response, redirect
import database as db
import time

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
    u = request.form['login']
    p = request.form['password']
    if db.verify_password(u, p):
        response = make_response(redirect('/'))
        response.set_cookie('username', u)
        return response
    else:
        time.sleep(3)
        return '''<p>incorrect password</p>
        <A HREF="javascript:javascript:history.go(-1)">Click here to go back to previous page</A>'''



@app.route('/logout/')
def logout():
    response = make_response(redirect('/'))
    response.set_cookie('username', expires=0)
    return response


@app.route('/user/<username>')
def get_user(username):
    return render_template('user.html', name=username)


if __name__ == '__main__':
    app.run(debug=True)
