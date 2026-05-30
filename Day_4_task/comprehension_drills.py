# List Comprehension Drills
# Demonstrates list, dictionary, and set comprehensions.

numbers = list(range(1, 21))

div_by_3 = [num for num in numbers if num % 3 == 0]

print("Numbers divisible by 3:")
print(div_by_3)

words = ["python", "java", "machine", "learning", "sql"]

long_words = [word.title() for word in words if len(word) > 4]

print("\nWords longer than 4 characters:")
print(long_words)

celsius = [0, 10, 20, 30, 40]

fahrenheit = [(temp * 9/5) + 32 for temp in celsius]

print("\nFahrenheit Temperatures:")
print(fahrenheit)

nested = [[1, 2], [3, 4], [5, 6], [7, 8]]

flattened = [item for sublist in nested for item in sublist]

print("\nFlattened List:")
print(flattened)

# Explore Section

dict_comp = {x: x**2 for x in range(1, 6)}
print("\nDictionary Comprehension:")
print(dict_comp)

set_comp = {x for x in range(1, 11) if x % 2 == 0}
print("\nSet Comprehension:")
print(set_comp)