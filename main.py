import os
from flask import Flask, render_template
from flask_mysqldb import MySQL
from dotenv import load_dotenv
from connect_planescape_db import *
from get_charlist import get_charlist
from get_charinfo import get_charinfo
from get_deadbooklist import get_deadbooklist
from get_deadbookcharinfo import get_deadbookcharinfo
load_dotenv('.env')

app = Flask(__name__)

mysql = connect_planescape_db(app)

# Test list of names
mylist = ["Garfield", "Odie"]


@app.route("/")
def hello_world():
    # Grab character names from database
    charlist = get_charlist(mysql)
    deadbooklist = get_deadbooklist(mysql)
    return render_template('index.html', mylist=sorted(charlist), deadbooklist=sorted(deadbooklist))


@app.route("/character/<string:charName>")
def char_page(charName):
    charinfo = get_charinfo(charName=charName, mysql=mysql)
    deadbooklist = get_deadbooklist(mysql)
    charlist = get_charlist(mysql)
    print(charinfo)
    return render_template('character_template.html', mylist=sorted(charlist), charinfo=charinfo, deadbooklist=sorted(deadbooklist))


@app.route("/story")
def story():
    charlist = get_charlist(mysql)
    deadbooklist = get_deadbooklist(mysql)
    return render_template('story.html', mylist=sorted(charlist), deadbooklist=sorted(deadbooklist))


@app.route("/deadbook/<string:charName>")
def deadbook(charName):
    charlist = get_charlist(mysql)
    deadbookcharinfo = get_deadbookcharinfo(mysql, charName=charName)
    deadbooklist = get_deadbooklist(mysql)
    return render_template('deadbook_template.html', mylist=sorted(charlist), deadbooklist=sorted(deadbooklist), deadbookcharinfo=deadbookcharinfo)

# 404 app handling


@app.errorhandler(404)
def page_not_found(e):
    charlist = get_charlist(mysql)
    deadbooklist = get_deadbooklist(mysql)
    return render_template('404.html', mylist=sorted(charlist), deadbooklist=sorted(deadbooklist)), 404

if __name__ == "__main__":
    app.run(host='0.0.0.0')