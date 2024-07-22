nums = [1, 1, 1, 2, 2, 3]
count = 1
for i in range(len(nums)-2):
    for j in range(len(nums)-1):
        if nums[i] == nums[j]:
            count += 1
    if count >2:
        print('dup')
