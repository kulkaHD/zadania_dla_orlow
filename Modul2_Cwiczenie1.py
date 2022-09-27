exam_points = {
  "Mariusz":30,
  "Mateusz":55,
  "Marta":76,
  "Roman":30,
  "Arleta":59,
  "Adrian": 96,
  "Monika":91,
  "Andrzej":22,
  "Krzysztof":83,
  "Krystyna":93,
  "Piotr":44,
  "Dawid":10,
  "Agnieszka":15
}

failed_students = []
top_students = []
best_student = (" ", )
max_points = 0
for name, points in exam_points.items():
  if points <= 45:
    failed_students.append(name)
  elif points >=91:
    top_students.append(name)
  if points >= max_points:
    max_points = points
    best_student = (name, points)


print(failed_students)
print(top_students)
print(best_student)