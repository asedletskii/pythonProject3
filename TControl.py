from TAbonent import TAbonent
from TAbonentList import TAbonentList

class TControl:
    def __init__(self):
        self.abonent_list = TAbonentList()
    
    def add_contact(self, name, number):
        self.abonent_list.add(TAbonent(name, number))
    
    def remove_contact(self, index):
        self.abonent_list.remove_by_index(index)
    
    def clear_contacts(self):
        self.abonent_list.clear()
    
    def find_contact(self, name, number):
        return self.abonent_list.find(name, number)
    
    def save_contacts(self, filename="contacts.json"):
        self.abonent_list.save_to_file(filename)
    
    def load_contacts(self, filename="contacts.json"):
        self.abonent_list.load_from_file(filename)