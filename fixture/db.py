
#import mysql.connector
import pymysql
from model.group import Group
from model.contact import Contact

class Dbfixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password)
        self.connection.autocommit(True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, lastname, firstname from addressbook")
            for row in cursor:
                (id, lastname, firstname) = row
                list.append(Contact(id=id, lastname=lastname, firstname=firstname))
        finally:
            cursor.close()
        return list

    def get_contact_list2(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select lastname, firstname from addressbook")
            for row in cursor:
                (lastname, firstname) = row
                list.append(Contact(lastname=lastname, firstname=firstname))
        finally:
            cursor.close()
        return list



    def destroy(self):
        self.connection.close()