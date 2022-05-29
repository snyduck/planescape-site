from flask import Flask, render_template
from flask_mysqldb import MySQL
from dotenv import load_dotenv
from connect_planescape_db import *
load_dotenv('.env')

import os

app = Flask(__name__)

mysql = connect_planescape_db(app)


# Test list of names
mylist = ["Garfield","Odie"]

@app.route("/")
def hello_world():
    #Grab character names from database
    charlist = []
    cur = mysql.connection.cursor()
    cur.execute('SELECT charName FROM planescape.charInfo;')
    rv = cur.fetchall()
    for i in rv:
        charlist.append(i[0])
    cur.close()
    return render_template('index.html',mylist=sorted(charlist))

@app.route("/character/<string:charName>")
def char_page(charName):
    charlist = []
    cur = mysql.connection.cursor()
    cur.execute('SELECT charName FROM planescape.charInfo;')
    rv = cur.fetchall()
    cur.execute(f'SELECT * FROM planescape.charInfo WHERE charName LIKE "{charName}%";')
    charinfo = cur.fetchall()
    for i in rv:
        charlist.append(i[0])
    print(charinfo)
    cur.close()
    return render_template('character_template.html',mylist=sorted(charlist),charinfo=charinfo)

@app.route("/story")
def story():
    charlist = []
    cur = mysql.connection.cursor()
    cur.execute('SELECT charName FROM planescape.charInfo;')
    rv = cur.fetchall()
    for i in rv:
        charlist.append(i[0])
    cur.close()
    return render_template('story.html',mylist=sorted(charlist))

@app.route("/deadbook")
def deadbook():
    charlist = []
    cur = mysql.connection.cursor()
    cur.execute('SELECT charName FROM planescape.charInfo;')
    rv = cur.fetchall()
    for i in rv:
        charlist.append(i[0])
    cur.close()
    return render_template('story.html',mylist=sorted(charlist))


if __name__ == "__main__":
    app.run(host='0.0.0.0')