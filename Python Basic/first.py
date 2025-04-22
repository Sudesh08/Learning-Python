# print("Hello World")

a, b, c = 3,3.6,"Sudesh" #this is possible in python
# print(a,b,c)
# print("the value of b is "+b) This will through error

# print("{}{}{}".format("The value of b is ",b," Yaha 1 or argument"))
# Data type in Python
# 1. Numeric data type
# 1.1 int
# 1.2 float
# 1.3 complex

# anything = 100+3j
# print(anything)

# 2. String ----->""

# 3. List ------> []
#A list is a data structure in Python that is a mutable, or changeable, ordered sequence of elements. Each element or value that is inside of a list is called an item. Just as strings are defined as characters between quotes, lists are defined by having values between square brackets [ ] .
#Need to go through the methods of List
value1=["Sudesh", 1, True,5.6,7,3,44,5]
# print(value1)
# print(value1[3])
# value1[3] = "Hello"
# print(value1[3])        #output 5.6
# print(value1[-1])       #output 5

# Append - Adds an item x to the end of the list
# value1.append("Last")  # It only takes one arguments
# print(value1)

#extends(iterable)- Extends the list by appending elements from another list
# value2 = ["Priya","Nainsi"]
# value1.extend(value2)
# print(value1)

#insert(i, x) - Inserts an item x at a given position i and it will increase the indexing suppose we have 3 elements after inserting any value the elements will be 4
# value1.insert(3,"middle")
# print(value1)

# remove(x) - Removes the first occurrence of x (x = value)
# value1.remove(3)
# print(value1)


# pop([i]) - Removes and returns item at position i (or last item if i is not provided)
# popvalue=value1.pop(4)
# print(value1,popvalue)

# clear()	Removes all items from the list
# value1.clear()
# print(value1)

# index(x[, start[, end]]) -	Returns the index of the first occurrence of x
# value3=["One","two","four","five","six","four","three","two","four","five","two","five"]
# print(value3.index("four"))
# print(value3.index("four",3))    #output 5


# reverse() -	Reverses the list in place
# value1.reverse()
# print(value1)

# 4. Tuple ------->()
#Similar to List the difference is we need to declare it inside () braces and touple is imutable(can't change)
# some example of touple
my_tuple = (1, 2, 3)
print(my_tuple)

# With parentheses
t1 = (10, 20, 30)

# Without parentheses (still a tuple)
t2 = 10, 20, 30

# Single-element tuple (must have a comma)
t3 = (5,)   # ✅ This is a tuple
t4 = (5)    # ❌ This is just an integer
print(t1,t2,t3,t4)
print(type(t4))


my_tuple = ("apple", "banana", "cherry")

print(my_tuple[1])       # Access by index → "banana"
print(len(my_tuple))     # Get length → 3
print("apple" in my_tuple) # Check existence → True

a, b, c = (1, 2, 3)
print(a, b, c)  # Output: 1 2 3

# 5. Dictionary ---->{}
# A dictionary in Python is an unordered collection of key-value pairs. It's super useful when you want to map one piece of data to another — like a name to a phone number
# It is similar to Object in JS

adress={
    "Fname" : "Sudesh" ,
    "Pincode" : 78288 ,
     3:"hello"
}
print(adress["Pincode"])
adress["Sname"]="Mahato"
print(adress)

del adress[3]
print(adress)

#to call the value we need to do like print(adress[Pincode])