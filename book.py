class Book:
    def __init__(self,book_id,title,publication_date,author,types):
        self.__book_id = book_id
        self.__title = title
        self.__publication_date = publication_date
        self.__type = types
        self.__author = author
        
    

    def __str__(self):
        return f"Book Id:\t{self.__book_id}\nTitle:\t{self.__title}\nPublication Date:{self.__publication_date}\nAuthor:\t{self.__author}"


    def get_bookid(self):
        return self.__book_id

    def get_title(self):
        return self.__title

    def get_publication_date(self):
        return self.__publication_date
    
    def get_author(self):
        return self.__author

    def set_author(self,author):
        self.__author=author


    def set_book_id(self,book_id):
        self.__book_id = book_id

    def set_title(self,title):
        self.__title = title

    def set_publication_date(self,publication_date):
        self.__publication_date = publication_date      

    def set_types (self,types):
        self.__type =types

    def get_types(self):
        return self.__type                 



                

