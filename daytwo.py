# Description: This file is for the second day of the python workshop


# create variables for the following :
# 1. age
age = 17
# 2. name
name = "Rando"
# 3. song
song = "Happy Bday"
# 4. food
food = "oranges"
# 5. number
number = 7
# #now include the variables you just made print in the following...

print("Once upon a time, there was a " + str(age) + " old coder named " + name)
print(name + " liked to hum the song " + song + " while coding. It was so annoying that their teammates would ")
print("throw " + food + " until " + name + " would stop singing.")
print('Still, '  + name + ' was the best coder on the team and could write ' + str(number) + ' lines of code every day.')
print('Maybe ' + song +'  was '+ name+ 's secret power?')
print('No one will ever know.')


# f string interpolation is a way to format strings in python
# What is syntax ? What is an algorithm?
#writing code that is correct & following the order. a set of instructions followed to solve a proble,=m
# what is a variable? What is a string?
# var holds data
#name = "Rando" #string that is defined
#age = is underfined cuz it has no value
# strings are nothing but plain text
# what does this do?
print("Giraffe \n academy")
#/n makes a new line
print("Giraffe \t academy")
#\t makes a tab
# or this

phrase = "python learning" #string 
phrase = str(phrase)
print(phrase + "is cool") 
#what does the + sign do? What is it called?
#this is called concentation 

#what if I wanted to get the length of a phrase?
print(f'the length of the phrase {len(phrase)}')


declarationOfIndependance = "The unanimous Declaration of the thirteen united States of America, When in the Course of human events, it becomes necessary for one people to dissolve the political bands which have connected them with another, and to assume among the powers of the earth, the separate and equal station to which the Laws of Nature and of Nature's God entitle them, a decent respect to the opinions of mankind requires that they should declare the causes which impel them to the separation."
declarationOfIndependance = str(declarationOfIndependance)
print(f'the length of the declaration is {len(declarationOfIndependance)}')
#what if I wanted to make the letters in the variable upper case or lower?




#what if I wanted to check and see if the phrase was all lower or upper?


#What if I wanted to get one letter of the phrase


# The names you use when creating these labels need to follow a few rules:
# 1. Names can not start with a number.
# 2. There can be no spaces in the name, use _ instead.
# 3. Can't use any of these symbols :'",<>/?|()!@#$%^&*~-+
# 4. It's considered best practice (PEP8) that names are lowercase.
# 5. Avoid using the characters 'l' (lowercase letter el), 'O' (uppercase letter oh), or 'I' (uppercase
# letter eye) as single character variable names.



# Working with numbers bold text
# We'll learn about the following topics:
# 1. Types of Numbers in Python
# 2. Basic Arithmetic
# 3. Differences between classic division and floor division


# Addition

# Subtraction

# Multiplication

# Division

# Modulus

# Exponentiation

# Floor Division

# Order of Operations followed in Python

# You can use parentheses to specify the order in which you want operations to be performed.

#to do more you need to import special math libraries from python
#from math import *
#this goes out and grabs some different math functions we can use
#floor method
#ceil method
#sqrt method
from math import * #import everything
print(floor(95.76666))
print(ceil(98.3333))
print(sqrt(54))


# Python has various "types" of numbers (numeric literals).
# 1. We'll mainly focus on integers and floating point numbers. Integers are just whole numbers,
# positive or negative. For example: 2 and -2 are examples of integers.
# 2. Floating point numbers in Python are notable because they have a decimal point in them, or
# use an exponential (e) to define the number. For example 2.0 and -2.1 are examples of
# floating point numbers. 4E2 (4 times 10 to the power of 2) is also an example of a floating
# point number in Python.



# challenge exerces... 
#create a program that asks for the user's name and age and then prints out the user's name and age

# create a program that asks for the user's name and then prints out the user's name in all caps

# create a program that asks for the user's name and then prints out the user's name in all lower case

# create a program that asks for price and then prints out the price with a 10% discount

# Given the phrase "Hancock High School", perform the following operations:
# Print the phrase with a newline character to separate "Hancock" and "High" and "School".
# Concatenate the phrase with " is cool", and print the result.
# Print the length of the phrase.
# Convert and print the phrase in uppercase and lowercase.
# Check if the phrase is all lower or all upper and print the result.
# Print the first and the last letter of the phrase.