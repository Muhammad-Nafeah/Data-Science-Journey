import numpy as np

#Data
# Rows = students, Columns = subjects (Math, English, Science, Urdu, Computer)
marks = np.array([
    [88, 76, 45, 90, 60],   # Ali
    [70, 55, 80, 65, 75],   # Osama
    [90, 88, 92, 85, 95],   # Mujtaba
    [40, 55, 60, 70, 45],   # Omar
    [78, 82, 70, 88, 91]    # Usman
])

def student_average():
    result = np.mean(marks,axis=1)
    return result

def subject_average():
    result = np.mean(marks,axis=0)
    return result

def highest_marks():
    result = np.max(marks)
    return result

def lowest_marks():
    result = np.min(marks)
    return result

def bonus_marks():
    result = marks[:, 2] + 5   # All rows, column 2
    return result

def above_70():
    result = marks[student_average() > 70]
    return result

def main():

    while True:
        print("\nStudent Marks Analyzer\n")

        print("1. Student Average")
        print("2. Subject Average")
        print("3. Highest Marks")
        print("4. Lowest Marks")
        print("5. Marks Above 70")
        print("6. Bonus Marks")
        print("7. Exit")

        choice: str = input("Enter your choice (1-7): ")

        match choice:
            case "1":
                print("Per Student Average Marks")
                print(student_average())
                print()
            case "2":
                print("Per Subject Average Marks")
                print(subject_average())
                print()
            case "3":
                print("Highest Marks")
                print(highest_marks())
                print()
            case "4":
                print("Lowest Marks")
                print(lowest_marks())
                print()
            case "5":
                print("Marks Above 70")
                print(above_70())
                print()
            case "6":
                print("Bonus Marks")
                print(bonus_marks())
                print()
            case _:
                print("Exiting....")
                break
main()



