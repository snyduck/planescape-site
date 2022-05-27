from flask import Flask, render_template
from flask_mysqldb import MySQL
from dotenv import load_dotenv
load_dotenv('/home/miguel/my_project/.env')

import os

app = Flask(__name__)

try:
    app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')
    app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
    app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
    app.config['MYSQL_DB'] = os.getenv('MYSQL_DB')
    mysql = MySQL(app)
except:
    print("Failure")


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
    return render_template('story.html',mylist=charlist)