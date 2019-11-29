class City:
    """classe city"""
    def __init__(self, dict):
        """ constructeur """
        self.name = None
        self.department = None
        self.country = None
        self.population = None
        self.mayor = None
        self.capital = None
        self.hydratation(dict)

    def hydratation(self, dict):
        """ creation d'une methode pour hydrater"""
        for key_name, value_name in dict.items():
            if hasattr(self, key_name):
                setattr(self, key_name, value_name)

    def show_location(self):
        """ creation de la methode show_location """
        print (" la ville de {} est dans le departement {}".format(self.ville, self.department))

    def change_location(self):
        """ creation de la methode change_location """
        print (" la ville de {} est dans le departement {}".format(self.ville, self.department))

    def show_information(self):
        """ creation d'une methode qui affiche tous les attribut de la ville"""
        text = "------------------\n \
        name: {}\n \
        department: {}\n \
        country: {}\n \
        population: {}\n \
        mayor: {}\n \
        capital: {}\n"
        print(text.format(self.name, self.department, self.country, self.population, self.mayor, self.capital))
