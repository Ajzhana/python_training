# -*- coding: utf-8 -*-
import pytest
from contact import contact
from application2 import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture
    
def test_add_contact(app):
    app.login("admin", "secret")
    app.init_contact_creation()
    app.fill_group_form(contact(firstname="1233", middlename="1232323", lastname="dftt", company="wddfdf", home="89655885558", address="dfrfrfff", mobile="855885485", email="dddddd",
                            address2="weeerdddd"))
    app.logout()

