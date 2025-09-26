# Step 1: Foundation Setup
student_name = "Ty Selles"
current_gpa = 3.2
social_points = 40
stress_level = 30
study_hours = 0
# Step 2: Course planning decision modifies study_hours and stress_level
choice = input("Do you want to take more courses? (yes/no): ").lower()

if choice == "yes":
    study_hours += 10
    stress_level += 20
    print("You took more courses: More study time, more stress!")
elif choice == "no":
    study_hours += 5
    stress_level += 5
    print("You kept your course load the same: Less stress, less study time.")
else:
    study_hours += 2
    stress_level += 10
    print("Invalid choice: Random schedule assigned.")
