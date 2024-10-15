from library import Library

l2 = Library("Main Library","Western Side","Muniirah")

print(l2.get_name())
l2.set_name("Sub Library")
print(l2.get_name())

print(l2.get_location())
l2.set_location("Eastern side")
print(l2.get_location())

print(l2.get_librarian())


