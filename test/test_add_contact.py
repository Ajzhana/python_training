# -*- coding: utf-8 -*-
from model.contact import contact
from sys import maxsize
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [
    contact(firstname=random_string("firstname", 10),
            middlename =random_string("middlename", 10),
            lastname=random_string("lastname", 10),
            company=random_string("company", 10),
            home=random_string("home", 10),
            address=random_string("address", 10),
            mobile=random_string("mobile", 10),
            email=random_string("email", 10),
            address2=random_string("address2", 10))

    for i in range(2)
   ]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.init_contact_creation()
    app.contact.fill_form(contact)
    app.contact.submit_form_creation()
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=contact.id_or_max) == sorted(new_contacts, key=contact.id_or_max)


