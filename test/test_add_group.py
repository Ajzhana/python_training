# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    old_groups = app.group.get_group_list()
    app.group.init_creation()
    app.group.fill_form(Group(name="ryryyr", header="rrr", footer="rrrr"))
    app.group.submit_creation()
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)

def test_add_empty_group(app):
    old_groups = app.group.get_group_list()
    app.group.init_creation()
    app.group.fill_form(Group(name="", header="", footer=""))
    app.group.submit_creation()
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)

