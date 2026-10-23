def calculate_grade(marks):
    if marks < 0 or marks > 100:
        return "Invalid marks"
    if marks >= 90:
        return "A"
    if marks >= 75:
        return "B"
    if marks >= 60:
        return "C"
    if marks >= 35:
        return "D"
    return "Fail"
def main():
    try:
        marks = int(input("Enter student marks: "))
        grade = calculate_grade(marks)
        print("Student Grade:", grade)
    except ValueError:
        print("Please enter a valid integer.")
if __name__ == "__main__":
    main()
