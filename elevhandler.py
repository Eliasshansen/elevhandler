import elev

class ElevHandler:

    def __init__(self):
        self.elevlista = []

    def print_meny(self):
        print()
        print ("\n\t\t\tMENY\n")
        print ("\n\t\t\t1.lista elever\n")
        print ("\n\t\t\t2.lägg till elev\n")
        print ("\n\t\t\t3.ta bort elev\n")
        print ("\n\t\t\t4. avsluta\n")
        
        val = input("gör ditt val:  ")

        return val
    

    def add_elev(self, elevnamn, utbildning, tel):
        t_elev = elev.Elev(elevnamn, utbildning, tel)
        self.elevlista.append(t_elev)
