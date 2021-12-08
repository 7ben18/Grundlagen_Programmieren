with open("09data") as f:
    nums = [int(x) for x in f.readlines()]

preamble = 25
failure = 0
rangefailure = 0

for i in range(preamble,len(nums),1):
    validate = False
    for a in range(i-preamble,i,1):
        for b in range(i-preamble, i, 1):
            if nums[a] != nums[b]:
                if nums[a] + nums[b] == nums[i]:
                    validate = True
    if not validate:
        failure = nums[i]
        rangefailure = i

print(failure)
# task 2
numslist = nums[0:rangefailure]
list = []

for i in range(len(numslist)):
    for a in range(i,len(numslist)):
        if sum(numslist[i:a]) == failure:
            list = numslist[i:a]
print(max(list) + min(list))

