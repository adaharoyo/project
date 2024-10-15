from librarian import Librarian 

l1 = Librarian("204","Waldah","Female","0756981023")



print(l1.get_name())
l1.set_name("Muniirah")
print(l1.get_name())

print(l1.get_gender())
print(l1.get_contact())


from library import Library

l2 = Library("Main Library","Western Side","Muniirah")

print(l2.get_name())
l2.set_name("Sub Library")
print(l2.get_name())
print(l2.get_location())
print(l2.get_librarian())


