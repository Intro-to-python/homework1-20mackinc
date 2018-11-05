Lloyd = {
  "name":"Lloyd",
  "homework":[90.0,97.0,75.0,92.0],
  "quizzes":[88.0,40.0,94.0],
  "tests":[75.0,90.0]
}

Alice = {
  "name":"Alice",
  "homework":[100.0,92.0,98.0,100.0],
  "quizzes":[82.0,83.0,91.0],
  "tests": [89.0,97.0]
}

Tyler = {
  "name":"Tyler",
  "homework":[0.0,87.0,75.0,22.0],
  "quizzes":[0.0,75.0,78.0],
  "tests":[100.0,100.0]
}

def average(numbers):
  total = sum(numbers)
  total = float(total)
  return total / len(numbers)

def get_final_grade(student):
  homework = average(student["homework"])
  quizzes = average(student["quizzes"])
  tests = average(student["tests"])
  return (homework * 0.1 + quizzes * 0.3 + tests * 0.6)

def get_letter_grade(score):
  if score >= 90:
    return "A"
  elif score >= 80:
    return "B"
  elif score >= 70:
    return "C"
  elif score >= 60:
    return "D"
  else:
    return "F"

def get_class_average(student_list):
  result_list = []
  for student in student_list:
    student_average = get_final_grade(student)
    result_list.append(student_average)
    return average(result_list)


students = [Lloyd, Alice, Tyler]

for i in students:
  print(i["name"])
  print("%s's grade is %s" % (i["name"], get_letter_grade(get_final_grade(i))))
  print()

class_average = get_class_average(students)

print("The class average is %s" %(class_average))
print("The average class letter grade is %s" %(get_letter_grade))
