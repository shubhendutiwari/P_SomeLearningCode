"""Write a function is_member() that takes a value (i.e. a number, string, etc) x and a list of values a, and returns True if x is a
member of a, False otherwise. (Note that this is exactly what the in operator does, but for the sake of the exercise you should pretend
 Python did not have this operator.)"""

def is_member(lst,value):
    for x in lst:
        if x==value:
            return True
        else:
            continue
    return False

lis = []
more_input = 'y'
while more_input == 'y':
    p = input ("Enter the value to add in list : ")
    lis.append (p)
    more_input = input ("Enter 'y' to add more element in list : ")

check_value = input ("Enter value to check in List : ")

print(is_member(lis, check_value))
