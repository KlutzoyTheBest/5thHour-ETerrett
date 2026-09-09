#Name: Ethan Terrett
#Class: 5th Hour
#Assignment: HW5
from pickle import APPEND

import pickle

#1. Print Hello World!

print("Hello World")

#1. Create a list with 5 strings containing 5 different names in it.

NameList = list(["Jake", "Mathew", "Isidro", "Vergil", "Dante"])

#2. Append a new name onto the Name List.

NameList.append("Jayden")

#3. Print out the 4th name on the list.

print(NameList[3])

#4. Create a list with 4 different integers in it.

NumList = [10, 20, 30, 50, 1000000000000000000000000]

#5. Insert a new integer into the 2nd spot and print the new list.

NumList.insert(1, 9498345)
print(NumList)

#6. Sort the list from lowest to highest and print the sorted list.

NumList.sort()
print(NumList)

#7. Add the 1st three numbers on the sorted list together and print the sum.

NumListSum = NumList[0] + NumList[1] + NumList[2]
print(NumListSum)

#8. Create a list with two strings, two variables, and too boolean values.

MixedList = list(["Howdy", "Cya", 2, 100, True, False])

#9. Create a print statement that asks the user to input their own index value for the list on #8.

MixedList.append(input("Please input whatever you feel: "))
