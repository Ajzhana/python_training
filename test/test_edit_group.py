

from model.group import Group
from random import randrange
import random

def test_modify_group_name(app, db):
    if len(db.get_group_list()) == 0:
        app.group.init_creation()
        app.group.fill_form(Group(name="Test"))
        app.group.submit_creation()
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    #index = randrange(len(old_groups))
    group_data = Group(name="New group")
    #group.id = old_groups[index].id
    app.group.modify_group_by_id(group_data, group.id)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups.count(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

#def test_modify_group_header(app):
#    if app.group.count() == 0:
#        app.group.init_creation()
#        app.group.fill_form(Group(header="Test"))
#        app.group.submit_creation()
#    old_groups = app.group.get_group_list()
#    app.group.modify_first_group(Group(header="New header"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)