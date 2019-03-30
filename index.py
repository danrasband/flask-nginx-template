import json

from flask import Flask, request, render_template


APP = Flask(__name__)

# APP.config['TEMPLATES_AUTO_RELOAD'] = True

@APP.route('/')
def default():
    '''Default response when hitting the / path.'''
    return render_template('index.html')
