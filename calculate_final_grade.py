def calculate_grade(homework, tests):
    weighted_homework = homework * 0.3
    weighted_tests = tests * 0.7
    final_grade = weighted_homework + weighted_tests
    return final_grade

homework = float(input("Enter your homework score: "))
tests = float(input("Enter your test score: "))
final_grade = calculate_grade(homework, tests)
print("Your final grade is:", final_grade)