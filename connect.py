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
    def get_link_userID(self,id):
        try:
            connection = sqlite3.connect(db)
            cursor = connection.cursor()
            cursor.execute(f"SELECT * FROM linklar WHERE user = {id}")
            a = cursor.fetchall()
            connection.close()
            return a
        except Exception as e:
            print(e)
    def get_link_catID(self,id):
        try:
            connection = sqlite3.connect(db)
            cursor = connection.cursor()
            cursor.execute(f"SELECT * FROM linklar WHERE category_id = {id}")
            a = cursor.fetchall()
            connection.close()
            return a
        except Exception as e:
            print(e)
    def get_link_text(self,text):
        connection = sqlite3.connect(db)
        cursor = connection.cursor()
        cursor.execute(f'SELECT * FROM linklar WHERE name LIKE "%{text}%"')
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
        connection = sqlite3.connect(db)
        cursor = connection.cursor()
        cursor.execute(f'INSERT INTO users(name,userID,username) VALUES("{name}",{userID},"{username}")')
        connection.commit()
        connection.close()

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
            # print("shu joyga keldi!")
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


if __name__ == '__main__':
    # dbs = Database()
    # # print(dbs.get_link())
    # dbs.set_link('aaa','','asdasda','asdas','a123123','bbbbb',1)
    # s = 0
    # n = 12
    # for i in range(n, 2 * n):
    #     s += (n + i) ** 3
    # print(s)
    a = 12;b=13;c = 1123;print(a,b,c)