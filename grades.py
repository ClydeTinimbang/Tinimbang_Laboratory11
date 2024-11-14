def get_grades():
    grades = []
    while True:
        grade = input("Enter grade for student: ")
        if grade.lower() == "done":
            return grades

        # Check if the input is a valid integer
        if grade.isdigit():
            grade = int(grade)
            if grade >= 40:
                grades.append(grade)
            else:
                print("Invalid input. Grades must be 40 or above.")
                break
        else:
            print("Invalid input. Please enter a number or 'done'.")
            break

# Get the grades from the user
grades = get_grades()

# Calculate the average grade
if grades:
    avg_grade = sum(grades) / len(grades)
    print(f"Average Grade: {avg_grade:.2f}")

    # Calculate the number of passing students (with a 75% passing grade)
    passing_stdnt = sum(1 for grade in grades if grade >= 75)
    print(f"Number of Students who passed: {passing_stdnt}")

    # Calculate the passing percentage
    passing_pct = (passing_stdnt / len(grades)) * 100
    print(f"Passing Percentage: {passing_pct:.2f}%")
else:
    print("No valid grades were entered.")