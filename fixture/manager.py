

from fixture.session2 import SessionHelper
from fixture.contact import ContactHelper

class Manager:

    def __init__(self, app):
        self.session = SessionHelper(self)
        self.contact = ContactHelper(self)
        self.app = app