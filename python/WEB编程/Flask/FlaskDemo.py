#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home1():
    return '<h1> 1 </h1>'

@app.route('/hello', methods=['GET'])
def home2():
    return '<h1> 2 </h1>'

@app.route('/world', methods=['GET'])
def home3():
    return "pass"

@app.route('/index', methods=['GET'])
def index():
    return {"msg" : "success"}

@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action = "/signin" method="post" >
    <p><input name="username"></p>
    <p><input name="password" type="password"></p>
    <p><button type="submit">Sign In</button></p>
    </form>'''

@app.route("/signin", methods=['POST'])
def signin():
    assert 1 == 2

    if request.form['username'] == 'admin' and request.form['password']=='password':
        return '<h3>Hello,admin!</h3>'

    return '<h3>Bad username or password </h3>'

if __name__ == '__main__' :
    app.run()


