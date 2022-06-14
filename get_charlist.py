from flask_mysqldb import MySQL
def get_charlist(mysql):
    charlist = []
    cur = mysql.connection.cursor()
    cur.execute('SELECT charName FROM planescape.charInfo WHERE deadbook = 0;')
    rv = cur.fetchall()
    for i in rv:
        charlist.append(i[0])
    cur.close()
    return charlist