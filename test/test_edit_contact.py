# -*- coding: utf-8 -*-
from model.contact import contact

def test_edit_contact_firstname(app):
    app.session.login("admin", "secret")
    app.contact.edit_contact(contact(firstname="New firstname"))
    app.session.logout()

def test_edit_contact_lastname(app):
    app.session.login("admin", "secret")
    app.contact.edit_contact(contact(lastname="New lastname"))
    app.session.logout()