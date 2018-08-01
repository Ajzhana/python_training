# -*- coding: utf-8 -*-
from model.contact import contact

def test_edit_contact(app):
    app.session.login("admin", "secret")
    app.contact.edit_contact(contact(firstname="Иван", middlename="Иванович", lastname="Иванов", company="wddfdf", home="", address="", mobile="", email="",
                          address2=""))
    app.session.logout()