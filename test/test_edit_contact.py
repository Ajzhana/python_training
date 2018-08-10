# -*- coding: utf-8 -*-
from model.contact import contact

def test_edit_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.init_contact_creation()
        app.contact.fill_form(contact(firstname="Test"))
        app.contact.submit_form_creation()
        app.contact.edit_contact(contact(firstname="New firstname"))

def test_edit_contact_lastname(app):
    if app.contact.count() == 0:
        app.contact.init_contact_creation()
        app.contact.fill_form(contact(lastname="Test"))
        app.contact.submit_form_creation()
    app.contact.edit_contact(contact(lastname="New lastname"))