from flask_mysqldb import MySQL
def get_charinfo(mysql,charName):
    cur = mysql.connection.cursor()
    cur.execute(f'SELECT * FROM planescape.charInfo WHERE charName LIKE "{charName}%";')
    charinfo = cur.fetchall()
    return charinfo