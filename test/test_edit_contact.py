# -*- coding: utf-8 -*-
from model.contact import contact
from random import randrange

def test_edit_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.init_contact_creation()
        app.contact.fill_form(contact(firstname="Test"))
        app.contact.submit_form_creation()
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    cont = contact(firstname="New firstname", lastname="New lastname")
    cont.id = old_contacts[index].id
    app.contact.edit_contact_by_index(cont, index)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = cont
    assert sorted(old_contacts, key=contact.id_or_max) == sorted(new_contacts, key=contact.id_or_max)

#def test_edit_contact_lastname(app):
#    if app.contact.count() == 0:
#        app.contact.init_contact_creation()
#        app.contact.fill_form(contact(lastname="Test"))
#        app.contact.submit_form_creation()
#    old_contacts = app.contact.get_contact_list()
#    app.contact.edit_contact(contact(lastname="New lastname"))
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) == len(new_contacts)