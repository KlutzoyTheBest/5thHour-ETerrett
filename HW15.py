#Name:Ethan Terrett
#Class: 5th Hour
#Assignment: HW15


#1. Create a for loop with variable i that counts down from 5 to 1 and then prints "Hello World!"
#at the end.
for i in range(5, 0, -1):
    print(i)
print("Hello World!")
#2. Create a for loop that counts up and prints only even numbers between 1 and 30.
for m in range(0, 31, 2):
    print(m)
#3. Create a for loop that prints from 1 to 30 and continues (skips the number) if the number is
#divisible by 3.
for d in range(0, 30):
    d += 1
    if d % 3 == 0:
        continue
    print(d)


#4. Create a for loop that prints 5 different animals from a list.
animals = ["Dog", "Cat", "Leopard", "Tiger", "Emu"]
for h in animals:
    print(h)
#5. Create a for loop that spells out a word you input backwards.
#(HINT: Google "How to reverse a string in Python")

for t in input("Give me a word: ")[::-1]:
    print(t)

#6. Create a list containing 10 integers of your choice and print the list.
numbers = [1, 345, 2, 645, 10, 12, 55, 100, 100000000, 7]
#7. Create two empty variables named evenNumbers and oddNumbers.
evenNumbers = []
oddNumbers = []
#8. Make a loop that counts the number of even and odd numbers in the list, and prints the
#result after the loop.

for m in numbers:
    if m % 2 == 0:
        evenNumbers.append(m)
    else:
        oddNumbers.append(m)
print(evenNumbers, oddNumbers)

#9. Create a variable that asks the user for an integer and an empty integer variable.
ask = int(input("Give me an integer: "))
empty_var = 1
#10. Create a loop with a range from 1 to the number the user input. Use the loop to find the
#factorial of that number and print the result. A factorial of a number is that number multiplied
#by every number before it until you reach 1. (For example: 5! is 5 x 4 x 3 x 2 x 1 = 120)
for f in range(1, ask + 1):
    empty_var *= f
    print(empty_var)
