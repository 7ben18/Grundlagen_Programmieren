with open("01data") as f:
    nums = f.readline()

cnt = 0
for i in range(len(nums)-1):
    if nums[i] == nums[i+1]:
        cnt += int(nums[i])

if nums[0:1] == nums[-1:]:
    cnt += int(nums[-1:])

print(cnt)