class Borrowing:
    def __init__(self,borrow_id,borrow_date,student,book_id,return_date,library_id):
        self.__borrow_id = ""
        self.__borrow_date = borrow_date
        self.__student = student
        self.__book_id = book_id
        self.__return_date = return_date
        self.__library_id = library_id

    def get_borrow_id(self):
        return self.__borrow_id

    def get_borrow_date(self):
        return self.__borrow_date

    def get_student(self):
        return self.__student

    def get_book_id(self):
        return self.__book_id

    def get_return_date(self):
        return self.__return_date

    def get_library_id(self):
        return self.__library_id

    def set_borrow_id(self,borrow_id):
        self.__borrow_id = borrow_id

    def set_borrow_date(self,borrow_date):
        self.__borrow_date = borrow_date

    def set_student(self,student):
        self.__student = student

    def set_book_id(self,book_id):
        self.__book_id = book_id

    def set_return_date(self,return_date):
        self.__return_date = return_date

    def set_library_id(self,library_id):
        self.__library_id = library_id                                                 
