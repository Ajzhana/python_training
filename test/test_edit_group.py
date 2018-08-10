

from model.group import Group

def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.init_creation()
        app.group.fill_form(Group(name="Test"))
        app.group.submit_creation()
    app.group.modify_first_group(Group(name="New group"))

def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.init_creation()
        app.group.fill_form(Group(header="Test"))
        app.group.submit_creation()
    app.group.modify_first_group(Group(header="New header"))