#indentation of code in python matters

print('hello world') # this will work
#    print('Hello world') # as it is a improper indentation it will not work

#the error that we get here is the unexpected indent error
#also proper usage of the ' and " is also something that we need to keep a track of

print("escaping the sequence using backslash \"+\" is also a good practice")
print('the other way is to use \' and \" to sepate them')

#using input
print('hello '+input("what is your name ? "))