"""Define a function overlapping() that takes two lists and returns True if they have at least one member in common, False otherwise.
 You may use your is_member() function, or the in operator, but for the sake of the exercise, you should (also) write it using two
 nested for-loops."""


def overlapping(lst1, lst2):
    for x in lst1:
        print(x)
        if x in lst2:
            return True
        else:
            continue
    return False

lis1 = []
more_input = 'y'
while more_input == 'y':
    p = input("Enter the value to add in list ONE : ")
    lis1.append(p)
    more_input = input("Enter 'y' to add more element in list : ")

lis2 = []
more_input = 'y'
while more_input == 'y':
    p = input("Enter the value to add in list TWO : ")
    lis2.append(p)
    more_input = input("Enter 'y' to add more element in list : ")

print(overlapping(lis1,lis2))