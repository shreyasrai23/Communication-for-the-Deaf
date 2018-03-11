import sqlite3
def enter(name,yesno):
    c = sqlite3.connect("data.db")
    cursor = c.cursor()
    try:
        cursor.execute("INSERT INTO DATA VALUES(?,?)",(name,yesno))
    except sqlite3.Error as e:
        print(e)
def get(name):
    c = sqlite3.connect("data.db")
    cursor = c.cursor()
    try:
        cursor.execute("select knows from data where name="+str(name))
    except sqlite3.Error as e:
        print(e)
    l = cursor.fetchall()
    return l[0][0]
