num1 = [1, 2, 2, 1]
num2 = [2, 2]
num3 = []

# Using O(n^2)
for i in range(len(num1)):
    for j in range(len(num2)):
        if (num1[i] == num2[j]) and (num1[i] not in num3):
            num3.append(num1[i])
print(num3)

# Using O(n)
set1 = set(num1)
set2 = set(num2)
inter = set1.intersection(set2)
print(list(inter))