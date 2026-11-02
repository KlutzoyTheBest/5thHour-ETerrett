#Name: Ethan Terrett
#Class: 5th Hour
#Assignment: HW14
import random, time

#1. Create a while loop with variable i that counts down from 5 to 0 and then prints
#"Hello World!" at the end.

i = 5
while i > 0:
    print(i)
    i -= 1
    time.sleep(0.4)
else:
    print("Hello World!")

#2. Create a while loop that prints only even numbers between 1 and 30 (HINT: modulo).
j = 1
while j <= 30:
    if j % 2 == 0:
        print(j)
    j += 1
    time.sleep(0.2)

#3. Create a while loop that prints from 1 to 30 and continues (skips the number) if the
#number is divisible by 3.
k = 1
while k < 30:
    k += 1
    if k % 3 == 0:
        continue
    time.sleep(0.4)
    print(k)

#4. Create a while loop that randomly generates a number between 1 and 6, prints the result,
#and then breaks the loop if it's a 1.

l = random.randint(1, 6)
while l < 7:
    if l == 1:
        break
    print(l)
    time.sleep(0.4)
    l = random.randint(1, 6)

#5. Create a while loop that asks for a number input until the user inputs the number 0.
m = input("please enter a number: ")
while m > "0":
    if m == "0":
        break
    m = input("please enter a number: ")
