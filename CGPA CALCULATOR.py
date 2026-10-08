print("===== CGPA Calculator =====")
print("Grade points: A=4.0, A-=3.7, B+=3.3, B=3.0, B-=2.7, C+=2.3, C=2.0, D=1.0, F=0.0")

def read_number(prompt, low, high):
    while True:
        try:
            value = float(input(prompt))
            if low <= value <= high:
                return value
            print(f"Enter a value between {low} and {high}.")
        except ValueError:
            print("Please enter a number.")

semesters = int(read_number("Number of semesters: ", 1, 12))
total_credits = 0
total_points = 0

for s in range(1, semesters + 1):
    n = int(read_number(f"\nNumber of courses in semester {s}: ", 1, 20))
    sem_credits = 0
    sem_points = 0
    courses = []

    for i in range(1, n + 1):
        name = input(f"\nCourse {i} name: ")
        grade = read_number("  Grade points (0.0 - 4.0): ", 0, 4)
        credits = read_number("  Credit hours (1 - 6): ", 1, 6)
        courses.append((name, grade, credits))
        sem_credits += credits
        sem_points += grade * credits

    print(f"\n--- Semester {s} Report ---")
    print(f"{'Course':<25}{'Grade':<10}{'Credits':<10}")
    for name, grade, credits in courses:
        print(f"{name:<25}{grade:<10}{credits:<10}")
    print(f"Semester GPA: {sem_points / sem_credits:.2f}")

    total_credits += sem_credits
    total_points += sem_points

print("\n==============================")
print(f"Total credits: {total_credits}")
print(f"Overall CGPA: {total_points / total_credits:.2f}")
