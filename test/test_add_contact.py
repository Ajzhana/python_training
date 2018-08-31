# -*- coding: utf-8 -*-
from model.contact import contact


def test_add_contact(app, data_contacts):
    cont = data_contacts
    old_contacts = app.contact.get_contact_list()
    app.contact.init_contact_creation()
    app.contact.fill_form(cont)
    app.contact.submit_form_creation()
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(cont)
    assert sorted(old_contacts, key=contact.id_or_max) == sorted(new_contacts, key=contact.id_or_max)


