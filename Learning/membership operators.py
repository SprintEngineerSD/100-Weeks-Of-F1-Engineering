#MEMBERSHIP OPERATORS= used to test whether a value or variable is found in a sequence
#                       1. in
#                       2. not in

#string example:
#word = "apple"
#letter = input("guess a letter in the secret word: ")
#if letter not in word:
#    print(f"{letter} was not found")
#else:
#    print(f"{letter} was found")



#set example:
#students = {"sponge", "patrick", "sandy"}
#student = input("Enter the student name: ")
#if student in students:
#    print(f"{student} was found")
#else:
#    print(f"{student} was not found")


#Dictionary example:
grades = {"sandy": "A","sponge":"B","squidward":"C", "patrick":"D" }
student = input("Enter the name of student: ")
if student in grades:
    print(f"{student}'s grades are {grades[student]}")
else:
    print(f"{student} was not found")
