import sys  

reload(sys)  
sys.setdefaultencoding('utf8')
import textile
import goi
from flask import render_template
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    index = open("index.html","r")
    return index.read()

@app.route('/sport/<sport>')
def goi_sport(sport):
    matches = open(sport+".txt", "r")
    ad = open("ad.txt", "r")
    page = ad.read() + textile.textile(matches.read())
    return page

