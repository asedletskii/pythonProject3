import json
from TAbonent import TAbonent

class TAbonentList:
    def __init__(self):
        self.contacts = []
    
    def add(self, abonent):
        self.contacts.append(abonent)
    
    def remove_by_index(self, index):
        if 0 <= index < len(self.contacts):
            del self.contacts[index]
    
    def clear(self):
        self.contacts.clear()
    
    def find(self, name, number):
        for i, abonent in enumerate(self.contacts):
            if name.lower() in abonent.name.lower() or number in abonent.number:  # Поиск по части строки
                return i
        return -1

    
    def to_list(self):
        return self.contacts
    
    def save_to_file(self, filename):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump([a.to_dict() for a in self.contacts], f, ensure_ascii=False, indent=4)
    
    def load_from_file(self, filename):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                self.contacts = [TAbonent.from_dict(d) for d in data]
        except FileNotFoundError:
            self.contacts = []