# Create a list variable fruits with three fruit names. Print the list.
fruits = ["Mango", "Apple", "Banana", "Orange", "Grapes", "Strawberry", "Kiwi"]
print(fruits)
# List items are indexed, the first item has index [0], the second item has index [1] etc.
print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[3])
print(type(fruits))
# The search will start at index 2 (included) and end at index 5 (not included).
print(fruits[2:5])
# By leaving out the end value, the range will go on to the end of the list:
print(fruits[:4])
print(fruits[3:])
print(fruits[-3:-1])
# Check if Item Exists
x = "Watermelon"
if x in fruits:
    print("{} is in the list" .format(x))
else:
    print("{} is not in list" .format(x))

# Change List Items: Add a new fruit to the list and print the updated list.
fruits[1:2] = ["Cherry", "Watermelon"]
print(fruits)
fruits.insert(2, "Blackberry")
print(fruits)

