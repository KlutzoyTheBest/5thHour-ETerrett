#Name: Ethan Terrett
#Class: 5th Hour
#Assignment: HW6
from statistics import median

#1. Create a list with 9 different numbers inside.

NumberList = [12, 39, 122, 90, 60, 20, 35, 1, 84]

#2. Sort the list from highest to lowest.

NumberList.sort(reverse=True)
print(NumberList)
#3. Create an empty list.

EmptyList = []

#4. Remove the median number from the first list and add it to the second list.

EmptyList.append(int(median(NumberList)))
NumberList.remove(int(median(NumberList)))

#5. Remove the first number from the first list and add it to the second list.

EmptyList.append(NumberList[0])
NumberList.remove(NumberList[0])

#6. Print both lists.

print(NumberList)
print(EmptyList)

#7. Add the two numbers in the second list together and print the result.

EmptyListSum = EmptyList[0] + EmptyList[1]
EmptyList.append(EmptyListSum)
print(EmptyListSum)

#8. Move the number back to the first list (like you did in #4 and #5 but reversed).

NumberList.append(int(EmptyList[2]))

#9. Sort the first list from lowest to highest and print it.

NumberList.sort()
print(NumberList)