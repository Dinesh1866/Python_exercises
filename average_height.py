student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
students_average = len(student_heights)
total_height = 0
for heights in student_heights:
      total_height += heights
print("total height = ",total_height)
average_height = total_height/students_average
print(round(average_height))