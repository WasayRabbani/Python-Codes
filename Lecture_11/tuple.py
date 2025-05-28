# Tuple


# 1. Empty Tuple
t1=()

# 2. Tuple Constructor
t2=tuple([1,2,3,'Asad',True])
print(t2)

# 3. Tuple Indexing
print(t2[1])

# 4. Tuple Slicing
print(t2[0:3])

# 5. Negative Slicing


# Negative Step
print(t2[-1:-5:-1])

# Positive Step
print(t2[-5:-1:1])

# 6. Deleting a tuple
del t2


# 7. Tuple Unpacking

tuple1=(1,2,3,4,5,6,7)
*a,b=tuple1
print(a)
print(type(a))


# 8. Join Tuple

t3=(1,2,3)
t4=(5,6,7)
t10=t3+t4
print(t10)

# 9. Changing items in a tuple

l2=list(t10)
l2.append('MindWired')
print(l2)
t10=tuple(l2)
print(t10)
print(type(t10))