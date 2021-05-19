
#grades = [85, 93, 45, 89, 85]
grades = []

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
