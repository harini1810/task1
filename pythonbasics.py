# Creating a list with initial elements
list1 = [1, 2, 3, 4]
print("Original list:", list1)  # Output: [1, 2, 3, 4]

# Adding an element to the list
list1.append(5)
print("List after adding 5:", list1)  # Output: [1, 2, 3, 4, 5]

# Removing an element from the list
list1.remove(4)
print("List after removing 4:", list1)  # Output: [1, 2, 3, 5]

# Modifying an element in the list
list1[1] = 7
print("List after changing the second element to 7:", list1)  # Output: [1, 7, 3, 5]

# Creating a dictionary with initial key-value pairs
dictionary = {"a": 1, "b": 2, "c": 3, "d": 4}
print("\nOriginal dictionary:", dictionary)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Adding a new key-value pair to the dictionary
dictionary["e"] = 5
print("Dictionary after adding ('e': 5):", dictionary)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# Removing a key-value pair from the dictionary
del dictionary["b"]
print("Dictionary after removing key 'b':", dictionary)  # Output: {'a': 1, 'c': 3, 'd': 4, 'e': 5}

# Modifying the value associated with a key in the dictionary
dictionary["c"] = 6
print("Dictionary after changing value of key 'c' to 6:", dictionary)  # Output: {'a': 1, 'c': 6, 'd': 4, 'e': 5}

# Creating a set with initial elements
set1 = {1, 2, 3, 4}
print("\nOriginal set:", set1)  # Output: {1, 2, 3, 4}

# Adding an element to the set
set1.add(5)
print("Set after adding 5:", set1)  # Output: {1, 2, 3, 4, 5}

# Removing an element from the set
set1.remove(2)
print("Set after removing 2:", set1)  # Output: {1, 3, 4, 5}

# Removing an element and adding a new one to modify the set
set1.remove(4)
set1.add(10)
print("Set after modifying:", set1)  # Output: {1, 3, 5, 10}
