#Name: Ethan Terrett
#Class: 5th Hour
#Assignment: HW8


#1. Import the "random" library

import random

#2. print "Hello World!"

print("hello world!")

#3. Create three different variables that each randomly generate an integer between 1 and 10

random_1 = random.randint(1, 10)
random_2 = random.randint(1, 10)
random_3 = random.randint(1, 10)

#4. Print the three variables from #3 on the same line.

print(random_1, random_2, random_3)

#5. Add 2 to the first variable in #3, Subtract 4 from the second variable in #3, and multiply by 1.5 the third variable in #3.

ran_add = random_1 + 2
ran_sub = random_2 - 4
ran_mult = random_3 * 1.5

#6. Print each result from #5 on the same line.

print(ran_add, ran_sub, ran_mult)

#7. Create a list containing four variables that each randomly generate an integer between 1 and 6

fun_list = [random.randint(1, 6), random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)]

#8. Sort the list in #7 and print it.

fun_list.sort()
print(fun_list)

#9. Add together the highest three numbers in the list from #7 and print the result.

add_list = fun_list[1] + fun_list[2] + fun_list[3]
print(add_list)

#10. Create a list with 5 names of other students in this class and print the list.

name_list = ["Jake", "Helber", "Cruz", "Oliver", "Gavin"]
print(name_list)

#11. Shuffle the list in #10 and print the list again.

random.shuffle(name_list)
print(name_list)

#12. Print a random choice from the list of names from #10.

choosing_name = random.choice(name_list)
print(choosing_name)