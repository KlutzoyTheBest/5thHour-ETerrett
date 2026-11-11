#Name:Ethan Terrett
#Class: 5th Hour
#Assignment: HW16


#1. import the "random" library
import random
#2. print "Hello World!"
print("Hello World!")
#3. Create three variables named a, b, and c, and allow the user to input an integer for each.

a = int(input("Give me a number: "))
b = int(input("Give me a number: "))
c = int(input("Give me a number: "))

#4. Add a and b together, then divide the sum by c. Print the result.
d = (a + b) / c
print(d)
#5. Round the result from #3 up or down, and then determine if it is even or odd.
n = round(d)
if n % 2 == 0:
    print("Even")
else:
    print("Odd")

#6. Create a list of five different random integers between 1 and 10.
randomness = [random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)]
#7. Print the 4th number in the list.
print(randomness[3])
#8. Append another integer to the end of the list, also random from 1 to 10.
randomness.append(random.randint(1, 10))
#9. Sort the list from lowest to highest and then print the 4th number in the list again.
randomness.sort()
print(randomness[3])
#10. Create a while loop that starts at 1, prints i and then adds i to itself until it is greater than 100.
i = 1
while i < 100:
    print(i)
    i += i
#11. Create a list containing the names of five other students in the classroom.
names = ["Oliver", "Wyatt", "Santi", "Jake", "Anthony"]
#12. Create a for loop that individually prints out the names of each student in the list.
for r in names:
    print(r)
#13. Create a for loop that counts from 1 to 100, but ends early if the number is a multiple of 10.
for m in range(1, 100):
    if m % 10 == 0:
        break
    print(m)
#14. Free space. Do something creative. :)
random_thing = random.randint(1, 100)
if random_thing % 10 == 0:
    print(random_thing)
    print("CHICKEN")
elif random_thing == 100:
    print(random_thing)
    print("Wow big number good job chicken")
else:
    print(random_thing)
    print("haha noob no number")

