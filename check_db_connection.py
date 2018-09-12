import pymysql.cursors
from fixture.db import Dbfixture


connection = Dbfixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    groups = Dbfixture.get_group_list()
    for group in groups:
        print(group)
    print(len(groups))
    #cursor=connection.cursor()
   # cursor.execute("select* from group_list")
    #for row in cursor.fetchall():
    #    print(row)
finally:
    Dbfixture.destroy()