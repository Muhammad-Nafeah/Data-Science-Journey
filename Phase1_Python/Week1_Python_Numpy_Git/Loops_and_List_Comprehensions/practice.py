# You have a list of 5 Pakistani cities:
# ["Karachi", "Lahore", "Islamabad", "Peshawar", "Quetta"]
# Print each city with its number like:
# 1. Karachi
# 2. Lahore
# 3. Islamabad


cities = ["Karachi", "Lahore", "Islamabad", "Peshawar", "Quetta"]

for index,city in enumerate(cities):

    print(f"{index+1}. {city}")

print("\n")



# Given this sentence:
# "My Name Is Abdul Nafeah"
# Loop through each character
# Print only the UPPERCASE letters on the same line
# Expected output: MNIAN


sentence = "My Name Is Abdul Nafeah"

for char in sentence:
    if char.isupper():
        print(char, end="")


print("\n")


# You have monthly savings in a tuple:
# (5000, 3000, 7000, 2000, 8000, 4000)
# Calculate total savings using a for loop
# Print total savings


monthly_savings = (5000, 3000, 7000, 2000, 8000, 4000)
total_savings = 0

for savings in monthly_savings:
    total_savings += savings

print(f"Total Savings: {total_savings}")

print("\n")


# Print all even numbers from 0 to 20
# using range() only
print("Even Numbers")
for i in range(20):
    if i % 2 == 0:
        print(i)



# Write a function called times_table
# It takes a number n
# It prints the multiplication table of that number from 1 to 10
# Example times_table(5):
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# ...
# 5 x 10 = 50


def TimesTable(n):
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")
    
TimesTable(5)



# Print a countdown from 10 to 1 using range()
# Then print "Go! 🚀"
# Expected output:
# 10 9 8 7 6 5 4 3 2 1
# Go! 🚀

for i in range(10,0,-1):
    print(i, end=" ")
print("\nGo!")


# You have 1000 rupees
# Every day you spend 150 rupees
# Use a while loop to print how much money you have each day
# Stop when you run out of money
# Expected output:
# Day 1: 850 rupees remaining
# Day 2: 700 rupees remaining
# Day 3: 550 rupees remaining
# ...


total_money = 1000
day = 0

while total_money > 0:
    day += 1

    if total_money < 150:
        remaining = total_money
        total_money = 0
        print(f"Day {day}: Only {remaining} rupees left — not enough for today!")
    else:
        total_money -= 150
        print(f"Day {day}: {total_money} rupees remaining")


# Write a number guessing game
# secret_number = 7
# Start guessing from 1 and keep incrementing
# Use a while loop to find the secret number
# Print "Checking: 1", "Checking: 2" etc
# When found print "Found it! The number is 7"


secret_number = 7
guess = 1

while guess != secret_number:

    print(f"Checking: {guess}")
    guess += 1

print(f"Found it! The number is {guess}")



# Given numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Using list comprehension create 3 new lists:
# 1. Square of every number    → [1, 4, 9, 16...]
# 2. Every number multiplied by 3 → [3, 6, 9, 12...]
# 3. Only odd numbers          → [1, 3, 5, 7, 9]


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#Square of every number
squared_list = [n**2 for n in numbers]
#Number multiplied by 3
cube_list = [n**3 for n in numbers]
#Odd Number List
odd_list = [n for n in numbers if n%2 == 1]

print(squared_list,"\n",cube_list,"\n",odd_list)


# Given this list of names:
# names = ["ahmed", "sara", "ali", "zara", "usman"]
# Using list comprehension:
# 1. Capitalize all names     → ["Ahmed", "Sara"...]
# 2. Get names longer than 3 letters → ["ahmed", "sara", "zara", "usman"]
# 3. Convert all to UPPERCASE → ["AHMED", "SARA"...]

names = ["ahmed", "sara", "ali", "zara", "usman"]
#Capitalize List
cap_names = [name.capitalize() for name in names]
#Longer than 3
longer_than_3 = [name for name in names if len(name) > 3]
#Uppecase List
upper_list = [name.upper() for name in names]

print(cap_names,"\n",longer_than_3,"\n",upper_list)


# Given temperatures in Celsius:
# temps = [10, 25, 37, 15, 42, 30, 8, 22]
# Using list comprehension:
# 1. Get only temperatures above 30  → [37, 42]
# 2. Convert ALL temps to Fahrenheit → formula: (c * 9/5) + 32
# 3. Get temps above 30 AND convert to Fahrenheit

temps = [10, 25, 37, 15, 42, 30, 8, 22]
#Above 30
temp_above_30 = [temp for temp in temps if temp > 30]
#To Fehrenheit
temp_to_fehrenheit = [(temp * 9/5) + 32 for temp in temps]
#Above 30 and To Fehrenheit
above_30_and_fehrenheit = [(temp * 9/5) + 32 for temp in temps if temp > 30]

print(temp_above_30,"\n",temp_to_fehrenheit,"\n",above_30_and_fehrenheit)


# Write the count_negatives function 3 ways:
# Way 1 — using a normal for loop
# Way 2 — using list comprehension + len()
# Way 3 — using list comprehension + sum()
# Test with: [-1, 5, -3, 0, -2, 8, -4]
# Expected output: 4

numbers = [-1, 5, -3, 0, -2, 8, -4]
count = 0
for n in numbers:
    if n < 0:
        count += 1
print("Output: ",count)    

negative_numbers = len([n for n in numbers if n < 0])
print("Output: ",negative_numbers)

negative_numbers = sum([1 for n in numbers if n < 0])
print("Output: ",negative_numbers)


# Write a function called fizzbuzz(n)
# Loop through numbers 1 to n
# If number is divisible by 3 → print "Fizz"
# If number is divisible by 5 → print "Buzz"
# If divisible by both 3 and 5 → print "FizzBuzz"
# Otherwise → print the number
# Test with fizzbuzz(20)

def fizzbuzz(n):
    for i in range(1,n+1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz!")
        elif i % 3 == 0:
            print("Fizz!")
        elif i % 5 == 0:
            print("Buzz!")
        else:
            print(i)
        
fizzbuzz(20)

def FIZZBUZZ(n):
    return ["FizzBuzz!" if i%3 == 0 and i%5 == 0
            else "Fizz" if i%3 == 0
            else "Buzz" if i%5 == 0
            else i
            for i in range(1,n+1)]
result = FIZZBUZZ(20)
print(result)
print(result.count("Fizz"))


# Using loops print this pattern:
# *
# **
# ***
# ****
# *****
# Then print it in reverse:
# *****
# ****
# ***
# **
# *
print("Forward")
for i in range(5): #for rows
    for j in range(i+1):  #for stars in that rows
        print("*",end="")
    print()
print("Reverse")
for i in range(5, 0, -1):
    for j in range(i):
        print("*",end="")
    print()



# 1
# 12
# 123
# 1234
# 12345

for i in range(5):
    for j in range(i+1):
        print(j+1, end="")
    print()


# 12345
# 1234
# 123
# 12
# 1

for i in range(5, 0, -1):
    for j in range(i):
        print(j+1,end="")
    print()


# A
# AB
# ABC
# ABCD
# ABCDE

for i in range(5):
    for j in range(i+1):
        print(chr(65 + j),end="")
    print()


#     *
#    **
#   ***
#  ****
# *****


for i in range(5):
    #for spaces
    for j in range(5 - i - 1):
        print(" ", end="")
    
    #for stars
    for j in range(i+1):
        print("*",end="")
    
    print()



#     *
#    ***
#   *****
#  *******
# *********

for i in range(5):
    #spaces
    for j in range(5 - i - 1):
        print(" ",end="")
    #stars
    for j in range(2*i + 1):
        print("*",end="")
    
    print()


# *********
#  *******
#   *****
#    ***
#     *

for i in range(5):
    #spaces
    for j in range(i):
        print(" ", end="")
    
    #stars
    for j in range(9 - (2*i)):
        print("*",end="")
    
    print()


# ['*', '**', '***', '****', '*****']

result = []
for i in range(5):
    stars = 1 * (i+1)
    result.append(stars)
print(result)

result = []
for i in range(5):
    result.append("*" * (i+1))

print(result)


# Given a sentence:
# sentence = "I am learning Python and Data Science in Karachi"
#
# Using loops and list comprehensions find:
# 1. Total number of words
# 2. All words longer than 4 letters
# 3. The longest word
# 4. Average word length
# 5. Print all words in UPPERCASE on one line


sentence = "I am learning Python and Data Science in Karachi"
words = sentence.split()
print(len(words))

longer_than_four = [word for word in words if len(word) > 4]
print(longer_than_four)

longest_word = max(words, key=len)
print(longest_word)

average_word_length = sum(len(word) for word in words)/len(words)
print(average_word_length)

uppercase_word = [word.upper() for word in words]
print(uppercase_word)

# 💡 convert list → sentence
# 👉 Use join()

sentence = " ".join(uppercase_word)
print(sentence)