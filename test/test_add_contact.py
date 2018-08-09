# -*- coding: utf-8 -*-
from model.contact import contact

def test_add_contact(app):
    app.contact.init_contact_creation()
    app.contact.fill_form(contact(firstname="1233", middlename="1232323", lastname="dftt", company="wddfdf", home="89655885558", address="dfrfrfff", mobile="855885485", email="dddddd",
                          address2="weeerdddd"))