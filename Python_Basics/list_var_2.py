# Add a new cars to the list and print the updated list.
cars = ["Toyota", "Mustang", "BMW", "Bugatti", "Tesla"]
# To add an item to the end of the list, use the append() method:
cars.append("Mercedes-Benz")
print(cars)

# To insert a list item at a specified index, use the insert() method.
cars.insert(2, "Audi Q5")
print(cars)

# To append elements from another list to the current list, use the extend() method.
updated_cars = ["Nissan Rogue", "Jeep Wrangler", "Volkswagen Golf"]
cars.extend(updated_cars)
print(cars)

# The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
new_list = ("Lamborghini", "Ferrari")
updated_cars.extend(new_list)
print(updated_cars)

# The remove() method removes the specified item.
cars.remove("Toyota")
print(cars)

# The pop() method removes the specified index.
cars.pop(2)
print(cars)

# If you do not specify the index, the pop() method removes the last item.
cars.pop()
print(cars)

# The del keyword also removes the specified index:
del cars[3]
print(cars)

# The del keyword can also delete the list completely.
del updated_cars

# The clear() method empties the list.
cars.clear()
print(cars)


