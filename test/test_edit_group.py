

from model.group import Group

def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.init_edit_first_group()
    app.group.fill_form(Group(name="ryryyr", header="rrr", footer="rrrr"))
    app.group.submit_update()
    app.session.logout()