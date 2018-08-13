from model.contact import contact

def test_del_contact(app):
    if app.contact.count() == 0:
        app.contact.init_contact_creation()
        app.contact.fill_form(contact(firstname="Test"))
        app.contact.submit_form_creation()
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_contact()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
