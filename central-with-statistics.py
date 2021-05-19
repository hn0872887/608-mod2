grades = [85, 93, 45, 89, 85]
grades = sorted(grades)
print("Grades list: " + str(grades))
count = len(grades)
print("Count value: " + str(count))
sum = sum(grades)
print("sum value: " + str(sum))
import statistics
print("mean is : " + str(statistics.mean(grades)))
print("median is : " + str(statistics.median(grades)))
print("mode is : " + str(statistics.mode(grades)))