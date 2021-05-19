import statistics
list = [*range (1, 101)]
print(list)
count = len(list)
print(count)
sum = sum(list)
print(sum)
mean = sum/count
print(mean)

print(statistics.mean(list))
print(statistics.median(list))
print(statistics.mode(list))
