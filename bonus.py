import statistics
list = [*range (1, 101)]
print(list)
count = len(list)
print(count)
sum = sum(list)
print(sum)
mean = sum/count
print(mean)

print("mean is: " + str(statistics.mean(list)))
print("median is: " + str(statistics.median(list)))
print("mode is: " + str(statistics.mode(list)))
