# Given this sentence:
# sentence = "i am learning data science and agentic ai in karachi"
#
# Using string methods:
# 1. Print it in ALL CAPS
# 2. Print it in Title Case (first letter of each word capitalized)
# 3. Print total number of characters including spaces
# 4. Check if sentence starts with "i am"
# 5. Check if sentence ends with "karachi"
# 6. Replace "karachi" with "pakistan"


sentence = "i am learning data science and agentic ai in karachi"

print(sentence.upper())
print(sentence.title())
print(len(sentence))
print(sentence.startswith('i am'))
print(sentence.endswith('karachi'))
print(sentence.replace('karachi','pakistan'))


# Given:
# name = "Syed Muhammad Abdul Nafeah"
#
# 1. Print only the first name "Syed"
# 2. Print only the last name "Nafeah"
# 3. Print the name in reverse
# 4. Print every second character of the full name


name = "Syed Muhammad Abdul Nafeah"
# | Method  | Use                           |
# | ------- | ----------------------------- |
# | slicing | position-based                |
# | split() | word-based (better for names) |   
#1st method                     
print(name[0:4])
#2nd method 
print(name.split()[0])

#1st method
print(name[-6:])
#2nd method 
print(name.split()[-1])

print(name[::-1])
print(name[::2])



# Given:
# date = "2024-11-25"
#
# 1. Split into year, month, day separately
# 2. Print each one:
#    Year: 2024
#    Month: 11
#    Day: 25
# 3. Rejoin them with "/" → "2024/11/25"
# 4. Rejoin them with " " → "2024 11 25"

date = "2024-11-25"
#unpacking
# 🧠 Rule of unpacking
# 👉 Number of variables = number of values
year,month,day = date.split("-")  #year,month,day = ["2024","11","25"] both are equal
print(date)

print("Year: {}".format(year))
print("Month: {}".format(month))
print("Day: {}".format(day))

new_date = "/".join([year,month,day])
print(new_date)
new_date = " ".join([year,month,day])
print(new_date)


# Given these variables:
# name = "Abdul Nafeah"
# university = "SSUET"
# year = 3
# cgpa = 3.567891
#
# Using .format() or f-string print:
# "My name is Abdul Nafeah, I study at SSUET"
# "I am in year 3 of my degree"
# "My CGPA is 3.57"   ← only 2 decimal places!


name = "Abdul Nafeah"
university = "SSUET"
year = 3
cgpa = 3.997464809

print(f"My name is {name}, I study at {university}")
print("I am in {} of my degree".format(year))
print("My CGPA is {:.2f}".format(cgpa))



# Given:
# sentence = "Data Science is Amazing"
#
# 1. Count how many vowels are in the sentence (a,e,i,o,u)
# 2. Print all consonants only on one line
# 3. Count how many spaces are in the sentence
# 4. Print each word on a new line using split()


sentence = "Data Science is Amazing"
vowels = "aeiouAEIOU"
count = 0

for char in sentence:
    if char in vowels:
        count += 1
print("Vowels: {}".format(count))


for char in sentence:
    if char not in vowels and char != " ":
        print(char,end=" ")

print("\n")

count = 0
for char in sentence:
    if char == " ":
        count += 1
print("Total Spaces: ",count)

words = sentence.split()
for word in words:
    print(word)




# Create a dictionary called student with:
# name, age, university, degree, year
# Use your own information
#
# 1. Print each key and value using .items()
# 2. Add a new key "city" with value "Karachi"
# 3. Update "year" to 4
# 4. Print all keys only
# 5. Print all values only
# 6. Check if "cgpa" is in the dictionary


student = {
    'name' : "nafeah",
    'age' : 22,
    'university': "Sir Syed University",
    'degree' : 'BCS',
    'year' : 3
}
print(student.items())

for k, v in student.items():
    print(k,v)

student['city'] = 'Karachi'

student['year'] = 4

print(student.keys())
for key in student.keys():
    print(key)

print(student.values())
for value in student.values():
    print(value)

print('cgpa' in student)


# Create a dictionary of 5 subjects and your marks:
# subjects = {
#     "Python": 88,
#     "Math": 75,
#     "English": 92,
#     "Physics": 68,
#     "DSA": 80
# }
#
# 1. Print each subject and mark like:
#    Python: 88
#    Math: 75
# 2. Find the highest mark
# 3. Find the lowest mark
# 4. Calculate average marks
# 5. Print subjects where marks are above 80


subjects = {
    "Python": 88,
    "Math": 75,
    "English": 92,
    "Physics": 68,
    "DSA": 80
}

for k,v in subjects.items():
    print(f"{k}: {v}")

print("Highest Marks: ", max(subjects.values()))

print("Lowest Marks: ", min(subjects.values()))

avg_marks = sum(subjects.values()) / len(subjects.values())
print("Average Marks: ",avg_marks)

for k, v in subjects.items():
    if v > 80:
        print(k,v)



# Given this list of cities and temperatures in Celsius:
# cities = ["Karachi", "Lahore", "Islamabad", "Peshawar", "Quetta"]
# temps =  [35,        28,        22,           25,         18]
#
# 1. Create a dictionary using zip:
#    {"Karachi": 35, "Lahore": 28 ...}
# 2. Using dictionary comprehension create a new dictionary
#    with temperatures converted to Fahrenheit
#    formula: (c * 9/5) + 32
# 3. Print each city with both Celsius and Fahrenheit like:
#    Karachi: 35°C = 95.0°F


cities = ["Karachi", "Lahore", "Islamabad", "Peshawar", "Quetta"]
temps =  [35,        28,        22,           25,         18]
#Method 01                         # We can also do the same using list
city_temps = dict(zip(cities,temps))
print(city_temps)
#Method 02
for city, temp in zip(cities,temps):
    print(f"{city} : {temp}", end=" ")

fehrenheit = {temp: (temp * 9/5) + 32 for temp in temps}
print("Fehrenheit: ",fehrenheit)


for city, temp in zip(cities,temps):
    print(f"{city} : {temp}C = {(temp * 9/5) + 32}F")


# Create a dictionary of 3 students:
# Each student has: name, age, and a list of 3 marks
#
# students = {
#     "student1": {"name": "Ahmed",  "age": 20, "marks": [88, 92, 75]},
#     "student2": {"name": "Sara",   "age": 19, "marks": [70, 65, 80]},
#     "student3": {"name": "Usman",  "age": 21, "marks": [95, 88, 92]},
# }
#
# Loop through and print for each student:
# Name: Ahmed | Age: 20 | Average: 85.0 | Pass/Fail


students = {
    "student1": {"name": "Ahmed",  "age": 20, "marks": [88, 92, 75]},
    "student2": {"name": "Sara",   "age": 19, "marks": [70, 65, 80]},
    "student3": {"name": "Usman",  "age": 21, "marks": [95, 88, 92]},
}
for k, v in students.items():
    name = v['name']
    age = v['age']
    marks = v['marks']

    avg_marks = sum(marks) / len(marks)

    if avg_marks >= 50:
        status = "Pass"
    else:
        status = "Fail"

    print(f"Name: {name} | Age: {age} | Average: {avg_marks} | {status}")



# Given this paragraph:
# text = "I am learning Python and Data Science.
#         Python is great for Data Science and AI.
#         I love Python"
#
# 1. Split into individual words
# 2. Create a dictionary where:
#    key = word
#    value = how many times it appears
# 3. Print each word and its count
# 4. Print the most repeated word


text = "I am learning Python and Data Science." 
"\nPython is great for Data Science and AI." 
"\nI love Python"

words = text.lower().replace(".","").replace("\n"," ")
words = words.split()
text_dictionary = {}

for word in words:
    if word == "":
        continue

    if word in text_dictionary:
        text_dictionary[word] += 1
    else:
        text_dictionary[word] = 1

for k, v in text_dictionary.items():
    print(f"{k}: {v}")


    
# 🧠 What is collections.Counter?

# 👉 It is a built-in tool that automatically counts items for you.

# Instead of writing:

# text_dictionary[word] += 1

# You just do 

# Counter(words)

from collections import Counter

word_count = Counter(words)
print(word_count)

repeated_word = word_count.most_common(1)[0][0]
print("Repeated Item: ",repeated_word)




# contacts = {
#     "Ahmed":  {"phone": "0300-1234567", "city": "Karachi"},
#     "Sara":   {"phone": "0311-2345678", "city": "Lahore"},
# }
# 1. Print all contacts neatly
# 2. Search contact by name
# 3. Add new contact
# 4. Delete a contact
# 5. Print all contacts from Karachi



contacts = {
    "Ahmed":  {"phone": "0300-1234567", "city": "Karachi"},
    "Sara":   {"phone": "0311-2345678", "city": "Lahore"},
    "Ali":    {"phone": "0321-3456789", "city": "Karachi"},
    "Zara":   {"phone": "0333-4567890", "city": "Islamabad"},
    "Usman":  {"phone": "0345-5678901", "city": "Peshawar"},
}

for k, v in contacts.items():

    print(f"Name: {k} | Phone: {v["phone"]} | City: {v["city"]} ")

search = "Ahmed"
if search in contacts:
    print("Contact Found!")

contacts["Mujtaba"] =  {"phone":"0345-5678991", "city":"Hyderabad"}
print("\n✅ Contact Added!")
print(contacts)


del contacts["Zara"]
print("\n✅ Contact Deleted!")
print(contacts)

for k, v in contacts.items():
    if v["city"] == "Karachi":
        print(k,v)



# Write caesar_cipher(text, shift) function
# Shift every letter by shift number
# Keep spaces as spaces
# Wrap around after "z"
# caesar_cipher("hello", 3)  → "khoor"
# caesar_cipher("khoor", -3) → "hello"



#ord() — Character → Number
#👉 ord() gives the ASCII / Unicode number of a character.

# chr() — Number → Character
# 👉 chr() does the reverse of ord()



def ceaser_cipher(text,shift):
    result = ""

    for char in text:
        if char == " ":
            result += " "
            continue
        elif char.isalpha():
            if char.islower():
                character_position = ord(char) - ord('a')   #Converts letter → number (0–25)
                new_position = (character_position + shift) % 26

                #Convert the number back to a letter:
                new_character = chr(new_position + ord('a'))
                result += new_character

            else:
                character_position = ord(char) - ord('A')   #Converts letter → number (0–25)
                new_position = (character_position + shift) % 26
                
                #Convert the number back to a letter:
                new_character = chr(new_position + ord('A'))
                result += new_character
        
    return result

encrypted_text = ceaser_cipher("Call me tonight", 3)
print("Encrypted Text: ",encrypted_text)




