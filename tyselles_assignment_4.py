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
# Step 3: Logical operators with study subjects
study_options = ["Programming", "Math", "English", "History"]
subject = input("Choose a subject to focus on (Programming/Math/English/History): ").title()

if subject in study_options:
    # Programming → high GPA if low stress AND GPA < 3.5
    if subject == "Programming" and stress_level < 50 and current_gpa < 3.5:
        current_gpa += 0.3
        social_points -= 5
        print("You mastered coding but sacrificed social life.")

    # Math OR English → smaller GPA boost OR social boost
    elif subject == "Math" or subject == "English":
        current_gpa += 0.1
        social_points += 5
        print("Balanced academics and social life.")

    # NOT History → History lowers stress, others raise it
    if subject not in ["History"]:
        stress_level += 5
    else:
        stress_level -= 5
        print("History was relaxing for you!")
else:
    print("Invalid subject choice! No changes made.")
# Step 4: Different endings using accumulated variables
if type(current_gpa) is not float:
    print("Error: GPA must be a float!")
else:
    if current_gpa >= 3.5:
        if stress_level < 40:
            print("Ending 1: Dean's List! Top grades, low stress, amazing semester!")
        else:
            print("Ending 2: Academic Star but Exhausted! High GPA but too much stress.")
    else:
        if social_points > 50:
            print("Ending 3: Social Butterfly! Fun semester, average academics.")
        else:
            print("Ending 4: Needs Improvement! Time to refocus next term.")

print(f"Adjusted GPA: {current_gpa}")
print(f"Adjusted Social Points: {social_points}")
print(f"Adjusted Stress Level: {stress_level}")
print(f"Adjusted Study Hours: {study_hours}")
