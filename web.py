import textile
import goi
from flask import render_template
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/cbb')
def goi_cbb():
    return textile.textile(render_template('cbb.html'))