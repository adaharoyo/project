class Bookcopy:
    def __init__(self,copy_id,book_id,library,status):
        self.__copy_id = copy_id
        self.__book_id = book_id
        self.__library = self.set_library_id(library)
        self.__is_available = self.set_status(True)

    def get_copy_id(self):
        return self.__copy_id

    def get_book_id(self):
        return self.__book_id

    def get_library(self):
        return self.__library

    def set_status(self,status):
        if status == "yes":
            self.__status = available

        else:
            print("Not available")


    def get_status(self):
        return self.__status                   