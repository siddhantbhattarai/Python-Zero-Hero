# - Create a boolean variable is_adult based on the age (x). 
# - Print a message saying whether the person is an adult or not.

age = int(input("Enter your age: "))
is_adult = age>=18
print(f"Are you adult? {is_adult}")