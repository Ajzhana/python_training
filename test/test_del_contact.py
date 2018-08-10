from model.contact import contact

def test_del_contact(app):
    if app.contact.count() == 0:
        app.contact.init_contact_creation()
        app.contact.fill_form(contact(firstname="Test"))
    app.contact.delete_contact()