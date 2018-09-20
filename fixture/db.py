
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

    def get_contact_list3(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, lastname, firstname, group_id from addressbook")
            for row in cursor:
                (id, lastname, firstname, group_id) = row
                list.append(Contact(id=id, lastname=lastname, firstname=firstname, group_id=group_id))
        finally:
            cursor.close()
        return list

    def get_contact_list2(self):
        self.list_contacts = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, email, email2, email3, mobile, home, work, phone2 from addressbook")
            for row in cursor:
                (id,  firstname, lastname, email, email2, email3, mobile, home, work, phone2) = row
                self.list_contacts.append(Contact(firstname=firstname, id=id, lastname=lastname,
                                                  homephone = home, mobile = mobile, workphone = work,
                                                  secondaryphone = phone2, email = email, email2 = email2, email3 = email3))
        finally:
            cursor.close()
        return list(self.list_contacts)



    def destroy(self):
        self.connection.close()