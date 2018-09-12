# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange
import random

def test_edit_contact_firstname(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.contact.init_contact_creation()
        app.contact.fill_form(Contact(firstname="Test"))
        app.contact.submit_form_creation()
    old_contacts = db.get_group_list()
    contact1 = random.choice(old_contacts)
    cont = Contact(firstname="New firstname", lastname="New lastname")
    #cont.id = old_contacts[index].id
    app.contact.edit_contact_by_id(cont, cont.id)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts.count(contact1)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


#def test_edit_contact_lastname(app):
#    if app.contact.count() == 0:
#        app.contact.init_contact_creation()
#        app.contact.fill_form(contact(lastname="Test"))
#        app.contact.submit_form_creation()
#    old_contacts = app.contact.get_contact_list()
#    app.contact.edit_contact(contact(lastname="New lastname"))
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) == len(new_contacts)