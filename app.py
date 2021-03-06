#!/usr/bin/env python

import os
from bottle import route, run, static_file, template, view, request, post

@route('/js/<filename>')
def js_static(filename):
    return static_file(filename, root='./js')

@route('/img/<filename>')
def img_static(filename):
    return static_file(filename, root='./img')

@route('/css/<filename>')
def img_static(filename):
    return static_file(filename, root='./css')

@route('/fonts/<filename>')
def fonts_static(filename):
    return static_file(filename, root='./fonts')

@route("/")
@view("main")
def hello():
    return dict(title = "Hello", content = "Hello from Python!")

@route('/suggestions.json')
def returnarray():
    from bottle import response
    from json import dumps
    rv = ['Hello','World','Hallo','Welt']
    response.content_type = 'application/json'
    return dumps(rv)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    run(host='0.0.0.0', port=port, reloader=True)