import sqlite3

def createTable():
    conn = sqlite3.connect('users.db')
    conn.execute('CREATE TABLE USERS (               \
                  Username varchar(255) NOT NULL,    \
                  Password varchar(255) NOT NULL,    \
                  Email varchar(255) NOT NULL,       \
                  FirstName varchar(255) NOT NULL);')

    conn.commit()
    conn.close()

def createUser(username, password, email, name):
    try:
        createTable()
    except:
        print("Table already created. Not creating a new one.")

    conn = sqlite3.connect('users.db')
    conn.execute("INSERT INTO USERS VALUES ('"+username+"','"+password+"','"+email+"', '"+name+"')")
    conn.commit()
    conn.close()

def contains(username, password):
    conn = sqlite3.connect('users.db')
    conn.execute("SELECT EXISTS(SELECT 1 FROM USERS WHERE Username='"+username+"' Password='"+password+"')") 
    conn.commit()
    conn.close()