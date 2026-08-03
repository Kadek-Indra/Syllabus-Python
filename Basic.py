# Basic collections (list,set,tuple)

# List (Mutable)
fruits =  ["apple", "watermelon", "peach", "lemons"]
fruits.append("Mango") # add new item
fruits[0] = "pineapple" # modify existing item

# Tuple (Immutable)
color = ("red", "yellow", "green", "pink", "yellow", "red")
yellow_count = color.count('yellow') # counting the amount of yellow color

# Set (Mutable and No duplicate)
numbers = {"5", "6", "7", "3"}
numbers.add("3") # duplicate will not be added
numbers.add("4")
removed_number = numbers.pop() # the number will appeared in random 

print (f"I have fruits, which are {fruits}, between these I have {yellow_count} fruits that the color is yellow")
print (f"The removed number from the set is {removed_number}")
