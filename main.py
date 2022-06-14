from flask import Flask, render_template
from flask_mysqldb import MySQL
from dotenv import load_dotenv
from connect_planescape_db import *
from get_charlist import get_charlist
from get_charinfo import get_charinfo
load_dotenv('.env')

import os

app = Flask(__name__)

mysql = connect_planescape_db(app)


# Test list of names
mylist = ["Garfield","Odie"]

@app.route("/")
def hello_world():
    #Grab character names from database
    charlist = get_charlist(mysql)
    return render_template('index.html',mylist=sorted(charlist))

@app.route("/character/<string:charName>")
def char_page(charName):
    charinfo = get_charinfo(charName=charName,mysql=mysql)
    charlist = get_charlist(mysql)
    print(charinfo)
    return render_template('character_template.html',mylist=sorted(charlist),charinfo=charinfo)

@app.route("/story")
def story():
    charlist = get_charlist(mysql)
    return render_template('story.html',mylist=sorted(charlist))

@app.route("/deadbook")
def deadbook():
    charlist = get_charlist(mysql)
    return render_template('story.html',mylist=sorted(charlist))


if __name__ == "__main__":
    app.run(host='0.0.0.0')