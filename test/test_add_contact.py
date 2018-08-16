# -*- coding: utf-8 -*-
from model.contact import contact
from sys import maxsize

def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    cont = contact(firstname="1233", middlename="1232323", lastname="dftt", company="wddfdf", home="89655885558", address="dfrfrfff", mobile="855885485", email="dddddd",
                          address2="weeerdddd")
    app.contact.init_contact_creation()
    app.contact.fill_form(cont)
    app.contact.submit_form_creation()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(cont)
    assert sorted(old_contacts, key=contact.id_or_max) == sorted(new_contacts, key=contact.id_or_max)


