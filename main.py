from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)

try:
    app.config['MYSQL_HOST'] = '10.0.30.7'
    app.config['MYSQL_USER'] = 'moonunit'
    app.config['MYSQL_PASSWORD'] = 'CY8p!NC-*UY+89vb'
    app.config['MYSQL_DB'] = 'gereg'
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
    cur.execute('SELECT charname FROM gereg.char_test;')
    rv = cur.fetchall()
    for i in rv:
        charlist.append(i[0])
    return render_template('index.html',mylist=charlist)

@app.route("/character/<string:charname>")
def char_page(charname):
    charlist = []
    cur = mysql.connection.cursor()
    cur.execute('SELECT charname FROM gereg.char_test;')
    rv = cur.fetchall()
    cur.execute(f'SELECT * FROM gereg.char_test WHERE charname LIKE "{charname}%";')
    charinfo = cur.fetchall()
    for i in rv:
        charlist.append(i[0])
    print(charinfo)
    return render_template('character_template.html',mylist=charlist,charinfo=charinfo)

@app.route("/story")
def story():
    charlist = []
    cur = mysql.connection.cursor()
    cur.execute('SELECT charname FROM gereg.char_test;')
    rv = cur.fetchall()
    for i in rv:
        charlist.append(i[0])
    return render_template('story.html',mylist=charlist)