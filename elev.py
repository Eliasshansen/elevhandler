class Elev:

    def __init__(self, namn, tel, utbildning):
        self.namn = namn
        self.tel = tel
        self.utbildning = utbildning

    def get_elev(self:):
        svar = self.namn+ "  |  program: +self.utbildning+ "  | Tel: "  + self.tel
    
        return svar 
