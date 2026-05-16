import numpy as np

# Create a NumPy array of 5 student marks
# Print the array
# Print the type
# Add 5 to all marks at once

student_marks = np.array([95,90,90,95,90,90])
print(student_marks)
print(type(student_marks))
print(f"Adding 5 to the array: {student_marks + 5}")


# Create a 1D array of 6 marks
# Print the first and last element
# Print elements from index 2 to 4
# Create a 2D array of 3 students and 3 subjects
# Print the second row
# Print the mark at row 2, column 1

marks = np.array([95,90,90,95,90,90])

print(marks[0],marks[-1])
print(marks[2:5])

two_dimensional_array = np.array([
    [90,97,88],
    [77,86,80],
    [75,67,80]
])
print(two_dimensional_array[1])
print(two_dimensional_array[1][0]) #or we can write its as [1,0]

# Create an array of 5 marks
# Add 5 bonus marks to all
# Create two arrays — math and english marks — add them together
# Filter and print only marks above 70

marks = np.array([95,90,90,40,90])
print(marks + 5)

math_marks = np.array([95,90,90,95,90])
english_marks = np.array([80,70,90,40,60])
print(math_marks + english_marks)

print(marks >= 50)
print(marks[marks > 70])


# Create an array of 5 marks
# Print sum, mean, min, max
# Create a 2D array of 3 students and 3 subjects
# Print average per student
# Print average per subject

marks = np.array([95,90,90,40,90])

print(np.sum(marks))
print(np.mean(marks))
print(np.max(marks))
print(np.min(marks))


two_dimensional_array = np.array([
    [90,97,88],
    [77,86,80],
    [75,67,80]
])
print(np.mean(two_dimensional_array,axis=1)) #row wise
print(np.mean(two_dimensional_array,axis=0)) #column wise

# Create a 1D array of 9 numbers
# Reshape it to 3x3
# Print the shape before and after
# Flatten it back to 1D

numbers = np.array([2,4,6,8,10,12,14,16,18])
print(numbers.shape)
reshape = numbers.reshape(3,3)
print(reshape)
print(reshape.shape)

flat = reshape.flatten()
print(flat)

# Create a 3x3 array of student marks
# Create a 1D array [5, 10, 15] as bonus marks per subject
# Add bonus to the classroom array
# Print the result

classroom = np.array([
    [88, 76, 45],
    [90, 60, 70],
    [55, 80, 95]
])
bonus_marks = np.array([5, 10, 15])

print(classroom + bonus_marks)

# Create an array of numbers from 1 to 20 with step 3.

array = np.arange(1,20,3) #start -> 1 , stop -> 20 not included , step -> 3
print(array)

#Create a 4x4 array of zeros and a 2x3 array of ones.
array = np.zeros((4,4))
print(array)

array = np.ones((2,3))
print(array)

# Create 6 evenly spaced numbers between 0 and 100.
array = np.linspace(0,100,6)  #Start → 0  , Stop → 100 (included) , How many numbers → 6
print(array)

#Create a 4x5 array of random marks between 40 and 100.
array = np.random.randint(40,100,(4,5)) #Low → 40 , High → 100 (not included) , Shape → (4, 5)
print(array)

# Create an array of 6 random marks and sort them in ascending and descending order.
array = np.random.randint(1,7,6) #Start -> 1 , Stop -> 7 not included , 6 -> 1D array of 6 elements
sorted_array = np.sort(array)
print(f"Sorted Array:  {sorted_array}")
reverse_sorted = np.sort(array)[::-1]
print(f"Unsorted Array:  {reverse_sorted}")


#Create an array of 5 marks and print the index of the highest and lowest mark.
marks_array = np.random.randint(1,20,5)
print(f"Array: {marks_array}")
highest_marks_index = np.argmax(marks_array)
print(f"Highest Marks Index: {highest_marks_index}")
lowest_marks_index = np.argmin(marks_array)
print(f"Lowest Marks Index: {lowest_marks_index}")



marks = np.array([88, 76, 45, 88, 60, 76, 34, 21, 44, 21, 34])
print(f"Marks: {marks}")
unique_marks = np.unique(marks)
print(f"Unique and Sorted Marks: {unique_marks}")

#Create an array of 6 marks and use np.where to label each as 'Pass' or 'Fail' (passing mark = 50).
marks = np.random.randint(40,100,6)
print(marks)
passing_marks = np.where(marks >= 50 ,'Pass','Fail')
print(passing_marks)

marks = np.array([110, 76, -5, 90, 60])
print(np.clip(marks,0,100))   #Any value above 100 → becomes 100 , Any value below 0 → becomes 0

#Create an array, make a copy using .copy(), change the first element of the copy, and prove the original is unchanged.

marks = np.array([88, 76, 45, 90, 60])
array1 = marks.copy()
array1[1] = 86
print("Original Array: ", marks)
print("New Array: ", array1)

