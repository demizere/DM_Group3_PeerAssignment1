# a program to test if a given list of element constitutes a set
List = ['Alex', 'Bob', 'Sam', 'Brian', 'Brian', 'Sam', 'Sam']
if len(List) == len(set(List)):
    print("true")
else:
    print("False" + str(",") + str("the set should be: ") + str(set(List)))