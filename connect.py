import sqlite3

db = "links.db"


class Database:
    def get_link(self):
        connection = sqlite3.connect(db)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM linklar")
        a = cursor.fetchall()
        connection.close()
        return a

    def get_link_userID(self, id):
        try:
            connection = sqlite3.connect(db)
            cursor = connection.cursor()
            cursor.execute(f"SELECT * FROM linklar WHERE user = {id}")
            a = cursor.fetchall()
            connection.close()
            return a
        except Exception as e:
            print(e)

    def get_link_catID(self, id):
        try:
            connection = sqlite3.connect(db)
            cursor = connection.cursor()
            cursor.execute(f"SELECT * FROM linklar WHERE category_id = {id}")
            a = cursor.fetchall()
            connection.close()
            return a
        except Exception as e:
            print(e)

    def get_link_text(self, text):
        connection = sqlite3.connect(db)
        cursor = connection.cursor()
        cursor.execute(f'SELECT * FROM linklar WHERE name LIKE "%{text}%" OR text LIKE "%{text}%"')
        a = cursor.fetchall()
        connection.close()
        return a

    def get_users(self):
        connection = sqlite3.connect(db)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users")
        b = cursor.fetchall()
        connection.close()
        return b

    def get_id(self):
        connection = sqlite3.connect(db)
        cursor = connection.cursor()
        cursor.execute("SELECT userID FROM users")
        b = cursor.fetchall()
        connection.close()
        return b

    def set_user(self, name, userID, username):
        try:
            connection = sqlite3.connect(db)
            cursor = connection.cursor()
            cursor.execute(f'INSERT INTO users(name,userID,username) VALUES("{name}",{userID},"{username}")')
            connection.commit()
            connection.close()
        except Exception:
            pass

    def set_link(self, text, photo, link, user, date, name, category_id):
        try:
            connection = sqlite3.connect(db)
            cursor = connection.cursor()
            cursor.execute(f'INSERT INTO linklar(text,photo,link,user,date,name,category_id)'
                           f'VALUES("{text}","{photo}","{link}","{user}","{date}","{name}",{category_id})')
            connection.commit()
            connection.close()
            return True
        except Exception as e:
            print(e)
            return False

    def get_admin(self):
        connection = sqlite3.connect(db)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM admins")
        a = cursor.fetchall()
        connection.close()
        return a

    def add_admin(self, name, userID, username):
        try:
            connection = sqlite3.connect(db)
            cursor = connection.cursor()
            cursor.execute(f'INSERT INTO admins(name,userid,username) VALUES("{name}",{userID},"{username}")')
            connection.commit()
            connection.close()
            return True
        except Exception as e:
            print(e)

    def add_link(self, text, photo, link, user, date, name, category_id):
        try:
            connection = sqlite3.connect(db)
            cursor = connection.cursor()
            cursor.execute(f'INSERT INTO linklar(text,photo,link,user,date,name,category_id)'
                           f'VALUES("{text}","{photo}","{link}","{user}","{date}","{name}",{category_id})')
            connection.commit()
            connection.close()
            return True
        except Exception as e:
            print(e)
            return False

    def delete_link(self, id):
        try:
            connection = sqlite3.connect(db)
            cursor = connection.cursor()
            cursor.execute(f"DELETE FROM linklar WHERE id={id}")
            connection.commit()
            connection.close()
            return True
        except Exception:
            return False

    def getID_link(self, id):
        try:
            connection = sqlite3.connect(db)
            cursor = connection.cursor()
            cursor.execute(f"SELECT * FROM linklar WHERE id={id}")
            a = cursor.fetchone()
            connection.close()
            return a
        except Exception:
            return False
