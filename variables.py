#variables are like the data that are saved that we can call on when we need it
# usually in python the naming convention follows snake case where we use the _ instead of spaces more or less similar to camel case from java
a = input("a: ")
b = input("b: ")

#exchanging the values
#approach 1 we can create a new variable to hold the value
c=a
a=b
b=c
print("After the initial swap")
print("a: "+a)
print("b: "+b)

#approach 2 we can use the inbuilt assignment
a,b=b,a

#print values
print("After the secondary swap")
print("a: "+a)
print("b: "+b)