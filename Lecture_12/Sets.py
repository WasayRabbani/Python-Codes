# Sets

'''Collection of well defined and distinct items.

1. Unordered
2. Changeable
3. Duplicates not allowed'''


# 1. Making Empty Set
s1=set()

# print(type(s1))


# 2. Making a Set

s2={54,32,76,85,32}
# print(s2)


# 3. Accessing Items in a set
s2=list( s2)
print(s2[0])
s2=set(s2)
 

# 4. Set Constructor

set3=set(['ABC',20,30.1,'Alex',100])
# print(set3)


# 5. Getting length of set

print(len(set3))


# Some useful Functions



# a. Adding one element to set
s1.add(30)
# print(s1)


# b. Adding multiple items to set
s1.update(['Alex',100,30,12,65,32,10,86])
print(s1)


# c. Removing item from set
s1.remove('Alex')
# print(s1)


# d. Removing Random Item of set 

s1.pop()
s1.pop()
# print(s1)


# e. Clearing Set / Empty it

# s1.clear()
# print(s1)


# f. Deleting a set

# del s1

# print(s1)


# g. Doing union operation on sets

s4=s1.union(set3)
print(s4)


# h. Doing intersection operation on sets

s4=s1.intersection(set3)
print(s4)


# i. Difference in two sets
print(s1.difference(set3))


# j. Checking subset

s1={1,2,3,4,5}
s2={1,2,3}
print(s2.issubset(s1))


# k. Checking if one set is a superset of another
s1={1,2,3,4,5}
s2={1,2,3}
print(s1.issuperset(s2))


# l. Copying a set

s5=s1.copy()

# print(s5)

s1.pop()
print(s1)
print(s5)

