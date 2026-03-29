# Create a list of 5 student names
# Print the first and last student
# Add a new student at the end
# Remove the second student
# Print the updated list and its length


students_list = ["Alice","Bob","Charlie","Smith","David"]
print(f"First student:{students_list[0]}")
print(f"Last student:{students_list[-1]}")

students_list.append("Sarah")
print(students_list)
students_list.pop(1)
print(students_list)
print(f"Updated Students List:{students_list}")
print(f"Length of Students List:{len(students_list)} students.\n\n\n")



# Create a list of 6 exam scores:
# [88, 92, 75, 60, 95, 83]
# Without using sum() or max() or min() manually:
# Print the highest score
# Print the lowest score
# Print the average score
# Print how many students scored above 80


exam_scores = [88, 92, 75, 60, 95, 83]

# Calculate the average score
total_score = 0
for total in exam_scores:
    total_score += total
average_score = total_score / len(exam_scores)
print(f"Average Exam Score: {average_score:.2f}")

# Find the highest and lowest scores without using max() and min()
highest_score = exam_scores[0]
for score in exam_scores:
    if score > highest_score:
        highest_score = score
print(f" Highest Exam Score: {highest_score}")

lowest_score = exam_scores[0]
for score in exam_scores:
    if score < lowest_score:
        lowest_score = score
print(f"Lowest Exam Score: {lowest_score}")

#Count scores above 80
count = 0
for score in exam_scores:
    if score > 80:
        count += 1
print(f"Number of scores above 80: {count}\n\n\n")


# Create this list:
# [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# Print the first 3 numbers
# Print the last 3 numbers
# Print every second number (10, 30, 50...)
# Print the list in reverse


numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(f"First 3 numbers: {numbers[0:3]}")
print(f"Last 3 numbers: {numbers[-3:]}")
print(f"Every second number: {numbers[::2]}")
print(f"Reversed List: {numbers[::-1]}\n\n\n")



import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Functions_and_Getting_Help.practice import CalculateGrade
def ReportCard(student_name, subject_scores):

    print(f"Report Card for Student:{student_name}")
    for index,score in enumerate(subject_scores):
        print(f"{index+1}. {score}")
    
    total = 0
    for score in subject_scores:
        total += score
    average_score = total // len(subject_scores)
    print(f"Average Score: {average_score}")

    #print(f"Average Score: {sum(subject_scores)//len(subject_scores)}")

    print(f"Grade: {CalculateGrade(average_score)}")

# Example usage:
ReportCard("Alice", [85, 92, 78, 90, 88])
    