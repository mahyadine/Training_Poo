class City:
    """classe city"""
    def __init__(self, ville, departement):
        """ constructeur """
        self.ville = ville
        self.departement = departement

    def show_location(self):
        """ creation de la methode show_location """
        print (" la ville de {} est dans le departement {}".format(self.ville, self.departement))

    def change_location(self):
        """ creation de la methode change_location """
        print (" la ville de {} est dans le departement {}".format(self.ville, self.departement))
