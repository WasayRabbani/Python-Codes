# List
l1=[1,2,3,4]


# 1. Empty List 
l2=[]


# 2. Adding multi Lists (concatenation)
l3=['x','y','z',1,2,3,4,5,6,7]
l4=l1+l3
print(l4)


# 3. Accessing List Items
print(l3[0])


# 4. Checking Length of List
print(len(l3))


# 5. Negative Indexing
print(l4[-1])


# 6. List Slicing
print(l3[0:5:2])
    

# 7. Negative Slicing
list1=[1,2,3,4,5,6,7,8,9,10]

# Left to right
print(list1[-10:-1])

# Right to Left
print(list1[-1:-11:-1])


# 8. Changing Items In List
list1[0]='MindWired'
print(list1)

# 9. Changing Items In List in Range
list1[0:4]=10,20,30,40
print(list1)


# 10. Insert Elements in list
list1.insert(0,'Mindwired')


# 11. Append Elements in list
list1.append('XYZ')


# 12. Remove Items from Lists
list1.remove('XYZ')
print(list1)
print(f"Latest {list1}")


# 13. Delete Items from List
del list1[0]
print(list1)
del list1 [1:4]
print(list1)
del list1
print(list1)


# 14. Extend  (adding list/tuple)
l5=[1,2,3]
l6=[1,2,3]
l5.extend(l6)
print(l5)

# 15. Copy Lists


# Copies list 6 elements to list 7 and makes list 7 a whole new list

l7=l6.copy()

# Makes reference of previous string
l7=l6
l6[0]='hh'
print(l7)




