
grades = [85, 93, 45, 89, 85]

count = len(grades)
print("count: " + str(count))
sum = sum(grades)
print("sum: " + str(sum))
mean = sum/count
print("mean: " + str(mean))


print("\n\n\n")
grades = sorted(grades)
print("after sorted: ")
print(grades)
if len(grades) % 2 == 0:
    median = (grades[len(grades) // 2 -1] + grades[len(grades) // 2]) / 2
else:
    median = grades[len(grades) // 2]

print("median: " + str(median))

print("\n\n\n")
tempGrades = []
countGrades = []
count = 1
tempGrade = 0
for grade in grades:
    if grade != tempGrade:
        count = count
        tempGrades.append(grade)
        countGrades.append(count)
    else:
        count = count + 1
        tempGrades.append(grade)
        countGrades.append(count)

print(tempGrades)
print(countGrades)
 