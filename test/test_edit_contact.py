# -*- coding: utf-8 -*-
from model.contact import contact

def test_edit_contact_firstname(app):
    app.contact.edit_contact(contact(firstname="New firstname"))

def test_edit_contact_lastname(app):
    app.contact.edit_contact(contact(lastname="New lastname"))