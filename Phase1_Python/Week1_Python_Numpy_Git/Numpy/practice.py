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