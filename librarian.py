class Librarian:
    def __init__(self,librian_id,name,gender,contact):
        self.__librian_id = librian_id
        self.__name = name
        self.__gender = gender
        self.__contact = contact


    def __str__(self):
        return f"Librarian Id:\t{self.librian_id}\nName:\t{self.name}\nGender:\t{self.gender}\nContact:\t{self.contact}"    



    def get_librarian_id(self):
        return self.__librian_id

    def get_name(self):
        return self.__name

    def get_gender(self):
        return self.__gender

    def get_contact(self):
        return self.__contact   

    def set_contact(self,contact):
        self.__contact = contact             

    def set_name(self,name):
        self.__name = name

    def set_gender(self,name):
        self.__gender

                