

from model.group import Group

def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.init_creation()
        app.group.fill_form(Group(name="Test"))
        app.group.submit_creation()
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(name="New group"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)

def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.init_creation()
        app.group.fill_form(Group(header="Test"))
        app.group.submit_creation()
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(header="New header"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)