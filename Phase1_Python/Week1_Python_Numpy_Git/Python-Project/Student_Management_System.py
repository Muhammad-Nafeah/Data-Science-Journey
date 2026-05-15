#Stuednts Data
students = {
    'Ali': {'Math':88,'Computer':80,'English':35,'Science':40,'Urdu':68},

    'Osama': {'Math':65,'Computer':80,'English':50,'Science':47,'Urdu':76},

    'Mujtaba': {'Math':88,'Computer':90,'English':80,'Science':79,'Urdu':80},

    'Omar': {'Math':90,'Computer':80,'English':70,'Science':50,'Urdu':69},

    'Usman': {'Math':78,'Computer':46,'English':47,'Science':91,'Urdu':51}
}

                                   
def calculate_average(student_name,show=True):

    subjects = students[student_name]
    average_marks = sum(subjects.values())/len(subjects.values())
    if show == True:
        print(f"Average Marks of {student_name} is : {average_marks}")
    return average_marks


def subject_status(student_name,show=True):
    fail_subjects = []

    for subject,marks in students[student_name].items():
        if marks >= 50:
            status = "Pass"
            if show == True:
                print(f"{subject}: {marks} -> ({status})")
        else:
            status = "Fail"
            fail_subjects.append(subject)
            if show == True:
                print(f"{subject}: {marks} -> ({status})")
    
    return fail_subjects

def overall_status(student_name):

    if calculate_average(student_name,show=False) < 50 or len(subject_status(student_name,show=False)) > 0:
        print("Overall Status: Fail")
    else:
        print("Overall Status: Pass")


def calculate_average_per_subject():
    subject_total = {}
    for student_name, subjects in students.items():
        for subject, marks in subjects.items():
            if subject not in subject_total:
                subject_total[subject] = marks
            else:
                subject_total[subject] += marks
    for subject, total_marks in subject_total.items():
        average_subject_marks = total_marks/len(students)
        print(f"{subject} average marks: {average_subject_marks}")


def top_three_leaderboard():
    student_average = {}
    for student_name in students:
        average = calculate_average(student_name,show=False)
        student_average[student_name] = average
    sorted_students = sorted(student_average.items(), key=lambda x:x[1],reverse=True)
    for rank, (name,average) in enumerate(sorted_students[:3]):
        print(f"Rank {rank+1}: {name} -> {average}")


def student_at_risk():
    for student_name in students:
        failed_subjects = subject_status(student_name,show=False)
        if len(failed_subjects) >= 2:
            print(f"{student_name} at Risk!")


def report_card(student_name):

    if student_name not in students:
        print("Student Not Found!")
        return

    subject_status(student_name)
    calculate_average(student_name)
    overall_status(student_name)

def main():

    while True:
        print("\nStudent Management System\n")

        print("1. Report Card")
        print("2. Class Average Per Subject")
        print("3. Top 3 Leaderboard")
        print("4. At Risk Students")
        print("5. Exit")

        choice: str = input("Enter your choice -> (1-5): ")

        match choice:
            case "1":
                student_name:str = input("Enter your name: ").title()
                print(f"Report Card of {student_name}")
                report_card(student_name)
                print()
            case "2":
                print("Class Average Per Subject")
                calculate_average_per_subject()
                print()
            case "3":
                print("Top 3 Leaderboard")
                top_three_leaderboard()
                print()

            case "4":
                print("At Risks Students")
                student_at_risk()
                print()
            case "5":
                print("Exiting.....")
                break
            case _:
                print("Invalid Choice!\nPlease enter a choice b/w 1 to 5")
                print()
main()





