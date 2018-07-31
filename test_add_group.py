# -*- coding: utf-8 -*-
import pytest
from group import Group
from application import Application

@pytest.fixture
def app(request):
   fixture = Application()
   request.addfinalizer(fixture.destroy)
   return fixture


def test_add_group(app):
    app.login(username="admin", password="secret")
    app.init_group_creation()
    app.fill_group_form(Group(name="ryryyr", header="rrr", footer="rrrr"))
    app.submit_group_creation()
    app.logout()

def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.init_group_creation()
    app.fill_group_form(Group(name="", header="", footer=""))
    app.submit_group_creation()
    app.logout()

