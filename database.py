import sqlite3

def createTable():
    conn = sqlite3.connect('login.db')
    conn.execute('CREATE TABLE USERS (               \
                  Username varchar(255) NOT NULL,    \
                  Password varchar(255) NOT NULL);')


    conn.commit()
    conn.close()

def createUser(username, password):
    conn = sqlite3.connect('login.db')
    conn.execute("INSERT INTO USERS VALUES ('"+username+"', '"+password+"')")
    conn.commit()
    conn.close()