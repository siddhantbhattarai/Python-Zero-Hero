# Question 11: Boolean Operations
is_raining = True
is_sunny = False
print(f"Is it a good day? {is_sunny or (not is_raining)}")

# Question 12: String Slicing
sentence = "Python is fun!"
print("First three characters:", sentence[:3])
print("Last three characters:", sentence[-3:])
print("Middle three characters:", sentence[len(sentence)//2 - 1:len(sentence)//2 + 2])

# Question 13: List Operations
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
common_elements = list(set(list1) & set(list2))
print("Common elements:", common_elements)

# Question 14: Type Conversion
num_str = "42"
num_int = int(num_str)
print("Converted to integer:", num_int)

# Question 15: Conditional Statements
temperature = 25
if temperature > 30:
    print("It's a hot day.")
elif 20 <= temperature <= 30:
    print("It's a moderate day.")
else:
    print("It's a cold day.")

# Question 16: Looping Through a List
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num * 2)

# Question 17: Dictionary Operations
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
merged_dict = {**dict1, **dict2}
print("Merged Dictionary:", merged_dict)

# Question 18: Formatting Numbers
price = 12.34
print(f"Price: ${price:.2f}")

# Question 19: List Comprehension
even_numbers = [num for num in range(1, 11) if num % 2 == 0]
print("Even Numbers:", even_numbers)

# Question 20: Multiple Assignments
a, b, c = 1, 2, 3
a, b, c = c, a, b
print("Swapped values:", a, b, c)
