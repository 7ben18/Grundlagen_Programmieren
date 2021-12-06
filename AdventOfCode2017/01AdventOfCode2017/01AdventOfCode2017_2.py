with open("01data_2") as f:
    nums = f.readline()
    #print(nums)

steps = len(nums) // 2
#print(steps)

cnt = 0
for i in range(len(nums)//2):
    if nums[i] == nums[i + steps]:
       cnt += int(nums[i]) + int(nums[i + steps])

print(cnt)

