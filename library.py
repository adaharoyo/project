class Library:
    def __init__(self,name,location,librarian):
        self.__name = name
        self.__location = location
        self.__librarian = librarian

    def __str_(self):
        return f"Name:\t{self.__name}\nLocation:\t{self.__location}\nLibrarian:\t{self.__librarian}"    






    def get_name(self):
        return self.__name

    def get_location(self):
        return self.__location

    def get_librarian(self):
        return self.__librarian


    def set_name(self,name):
        self.__name = name

    def set_location(self,location):
        self.__location = location

    def set_librarian(self,librarian):
        self.__librarian = librarian                        