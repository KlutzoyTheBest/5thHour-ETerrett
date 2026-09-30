#Name: Ethan Terrett
#Class: 5th Hour
#Assignment: HW9

#1. Print Hello World!
print("Hello world!")
#2. Create a dictionary with 3 keys and a value for each key. One of the keys must have a value with a list containing
#three numbers inside.
thingamabob = {
    "Numbers1" : [1, 2, 3],
    "Numbers2" : [4],
    "Numbers3" : [5]
}
#3. Print the keys of the dictionary from #2.
print(thingamabob.keys())
#4. Print the values of the dictionary from #2
print(thingamabob.values())
#5. Print one of the three numbers from the list by itself
print(thingamabob["Numbers1"][2])
#6. Using the update function, add a fourth key to the dictionary and give it a value.
thingamabob.update({"Numbers4" : [6]})
#7. Print the entire dictionary from #2 with the updated key and value.
print(thingamabob)
#8. Make a nested dictionary with three entries containing the name of another classmate and two other pieces of information
#within each entry.
nest_dict = {
    "Student1" : {
        "Name" : "Jake",
        "Sports" : True,
        "A bum" : True,
    },
    "Student2" : {
        "Name" : "Cruz",
        "Sports" : True,
        "A bum" : "Sometimes",
    },
    "Student3" : {
        "Name" : "Oliver",
        "Sports" : True,
        "A bum" : True,
    },
}
#9. Print the names of all three classmates on the same line.
print(nest_dict)
#10. Use the pop function to remove one of the nested dictionaries inside and print the full dictionary from #8.
nest_dict.pop("Student2")
print(nest_dict)