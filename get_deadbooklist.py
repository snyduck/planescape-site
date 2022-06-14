from flask_mysqldb import MySQL
def get_deadbooklist(mysql):
    charlist = []
    cur = mysql.connection.cursor()
    cur.execute('SELECT charName FROM planescape.charInfo WHERE deadbook = 1;')
    rv = cur.fetchall()
    for i in rv:
        charlist.append(i[0])
    cur.close()
    return charlist