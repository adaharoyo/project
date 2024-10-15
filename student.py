class Student:
    def __init__(self,studentid,name,course,year,faculty,gender):
        self.__studentid = studentid
        self.__name = name
        self.__course = course
        self.__year = year
        self.__faculty = faculty
        self.__gender = gender

    def __str_(self):
        return f"Student Id:\t{self.studentid}\nName:\t{self.name}\nCourse:\t{self.course}\nYear:\t{self.year}\nFaculty:\t{self.faculty}\nGender:\t{self.gender}"

    def get_studentid(self):
        return self.__studentid

    def get_name(self):
        return self.__name

    def get_course(self):
        return self.__course

    def get_year(self):
        return self.__year

    def get_faculty(self):
        return self.__faculty

    def get_gender(self):
        return self.__gender

    def set_studentid(self,studentid):
        self.__studentid = studentid

    def set_name(self,name):
        self.__name = name

    def set_course(self,course):
        self.__course = course

    def set_year(self,year):
        self.__year = year

    def set_faculty(self,faculty):
        self.__faculty = faculty

    def set_gender(self,gender):
        self.__gender = gender                        
