# Dictionary in Python

'''

A dictionary in Python is a collection of key-value pairs.

Each key is unique.

You use a key to get its corresponding value.

Dictionaries are ordered,changeable & they don't allow duplicates.

'''

# 1. Making a Dictionary

dict1={'Name':'Ali','Class':8,'Gender':'Male','Age':15}
# print(dict1)


# 2.  Getting Length of a Dictionary
print(len(dict1))


# 3. Dictionary Construction
dict=dict(name='Sara',Age=25,Gender='Female')
# print(dict)


# 4. Changing Values in Dictionary
dict1['Salary']=20000
# print(dict1)


# 5. Checking whether a key is in dictionary or not

# print(dict1.get('ZYX')) # if key not in dictionary, gives output none


# 6. Updating a dictionary

dict1.update(dict)
# print(dict1)


# 7. Deleting Keys in a dictionary

del dict1['Gender']
# print(dict1)


# 8. Nested Dictionary

d3={'Data':dict1}
d4={'Name':{'Name':'Zafar','Gender':'Male'}}
# print(d4)


# Some useful Functions

print(dict1)


# 1. get(key)	Returns the value of a key 

print(dict1.get('Class'))


# 2. keys()	Returns all keys

print(dict1.keys())


# 3. values()	Returns all values

print(dict1.values())


# 4. items()	Returns all key-value pairs

print(dict1.items())


# 5. pop(key)	Removes item with specified key

(dict1.pop('Salary'))
print(dict1)


# 6. popitem()	Removes last inserted item

(dict1.popitem())
print(dict1)


# 7. clear()	Empties the dictionary

dictionary=dict(name='Ali')
dictionary.clear()


# 8. update()	Adds items from another dictionary

dict1.update(dict)


# 9. copy()	Returns a shallow copy of the dictionary

d2=dict1.copy()
print(f'Dictionary New {d2}')


