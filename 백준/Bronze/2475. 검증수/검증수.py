nums = list(map(int, input().split(' ')))
sum = 0
for i in range(len(nums)):
    sum += nums[i] * nums[i]
print(sum % 10)