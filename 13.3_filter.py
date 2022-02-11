#You are analyzing a data set of animals. The data is a list of numbers, which represent the ages of animals.
# You need to take a number as input and output how many of the animals are older than the given number. 


ages = [3, 1, 9, 0.4, 7, 12, 2, 1.7, 5.7, 42, 6.7, 14.5, 21]
num = int(input())

res = len(list(filter(lambda x: x > num , ages)))

print(res)