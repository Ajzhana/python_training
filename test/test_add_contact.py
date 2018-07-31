# -*- coding: utf-8 -*-
import pytest
from model.contact import contact
from fixture.application2 import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture
    
def test_add_contact(app):
    app.session.login("admin", "secret")
    app.group.init_contact_creation()
    app.group.fill_form(contact(firstname="1233", middlename="1232323", lastname="dftt", company="wddfdf", home="89655885558", address="dfrfrfff", mobile="855885485", email="dddddd",
                          address2="weeerdddd"))
    app.session.logout()

