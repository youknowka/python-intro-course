﻿#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# A very simple Flask Hello World app for you to get started with...

import flask
from flask import Flask, request

app = Flask(__name__, static_folder="static", static_url_path="", template_folder="templates")

@app.route('/hello/<string:text>')
@app.route('/hello')
def hello_world(text=None):
    return 'Just a plain text: "Hello from Flask!"' + (' With param ' + text if text else '')


@app.route('/')
def root():
    return flask.render_template(
        'index.html'
    )


@app.route('/name', methods = ['GET', 'POST'])
def hello_name():
    if request.method == 'GET':
        name_param=request.args.get('name')
    elif request.method == 'POST':
        name_param=request.form.get('name')

    if name_param==None:
        name_param="Anonymous"

    return flask.render_template(
        'name.html',
        name=name_param
    )

if __name__ == '__main__':
   # print(app.config['STATIC_FOLDER'])
   app.run(debug = True)