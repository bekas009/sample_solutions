# input data and split
data = input().split()
# sorted data
data.sort()
# find and sorted unique data
unique = set(data)
# unique = sorted(unique)
# print(data)
for i in unique:
    print (data.count(i), i)