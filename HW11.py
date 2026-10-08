#Name: Ethan Terrett
#Class: 5th Hour
#Assignment: HW11

import random

#1. Print "Hello World!"
print("Hello world")
#2. Create a list with three values that each randomly generate a number between 1 and 100
list_a = [random.randint(1,100), random.randint(1,100), random.randint(1,100)]
#3. Print the list.
print(list_a)
#4. Create an if statement that determines which of the three numbers is the highest and prints the result.
if list_a[0] >= list_a[1] and list_a[0] >= list_a[2]:
    print(list_a[0])
    num = list_a[0]
elif list_a[1] >= list_a[2] and list_a[1] >= list_a[0]:
    print(list_a[1])
    num = list_a[1]
else:
    print(list_a[2])
    num = list_a[2]
#5. Tie the result (the largest number) from #4 to a variable called "num".

#6. Create a nested if statement that prints if num is divisible by 2, divisible by 3, both, or neither.
if num % 2 == 0:
    if num % 3 == 0:
        print("num is divisible by 3")
    else:
        print("num is divisible by 2, but not 3")
else:
    print("num isn't divisible by either")