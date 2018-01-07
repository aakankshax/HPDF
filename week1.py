# -*- coding: utf-8 -*-

from flask import Flask, render_template, make_response
from flask import request
import requests
import sys

app = Flask(__name__)

@app.route('/')
def hello():
       return 'Hello World - Aakanksha'


@app.route('/authors', methods=['GET'])
def authors():
    data = requests.get('https://jsonplaceholder.typicode.com/users').json()
    posts = requests.get('https://jsonplaceholder.typicode.com/posts').json()
    users = {d['id']:{'name':d['name'],'count':0} for d in data}
    for post in posts:
        users[post['userId']]['count']+=1
    return render_template('authors.html', users=users)


@app.route('/inputcookie')
def inputcookie():
    return render_template('cookie.html')

@app.route('/setcookie', methods = ['POST', 'GET'])
def cookie_insertion():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
    
    resp = make_response('Cookie values set!')
    resp.set_cookie('name', name)
    resp.set_cookie('age', age)
    return resp

@app.route('/getcookie')
def get_cookie():
    name = request.cookies.get('name')
    age = request.cookies.get('age')
    return 'Name: ' + name + ' and Age:  ' + age


@app.route('/robots.txt')
def view():
    response = make_response('YOU SHOULDN’T BE HERE')

    return response


@app.route('/html')
def static_page():
    return render_template('text.html')


@app.route('/input')
def input():
    return(render_template('input.html'))

	
@app.route('/display', methods = ['POST', 'GET'])
def display():
   if request.method == 'POST':
       user = request.form['post']
       print(user, sys.stdout.write)
   return 'Output is on terminal'
   

if __name__ == '__main__':
    app.run()




