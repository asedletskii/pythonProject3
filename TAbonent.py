# Класс TAbonent (Абонент)
class TAbonent:
    def __init__(self, name, number):
        self.name = name
        self.number = number
    
    def to_dict(self):
        return {"name": self.name, "number": self.number}
    
    @staticmethod
    def from_dict(data):
        return TAbonent(data["name"], data["number"])