# Input student's name
student_name = input("Enter Student's Name: ")

# Input grades
prelim_grade = float(input("Enter Prelim Grade: "))
midterm_grade = float(input("Enter Midterm Grade: "))
final_grade = float(input("Enter Final Grade: "))

# Compute final average
final_average = (prelim_grade + midterm_grade + final_grade) / 3

# Display result
print("\n" + student_name)
print(f"Final Average: {final_average:.2f}")

if final_average >= 75:
    print("Passed")
else:
    print("Failed")
