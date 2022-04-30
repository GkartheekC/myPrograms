


nums = [1, 0, 1]
zeroNum = 0
zeroCheck = len(nums)


for i in nums:
    if i == 0:
        zeroNum += 1



        
while zeroNum > 0:
    for k in range(zeroCheck):
        print(k)
        if nums[k] == 0:
            for l in range(k, zeroCheck):
                if l != zeroCheck - 1:
                    nums[l] = nums[l+1]

                else:
                    nums[zeroCheck - 1] = 0
                
                
        

            zeroNum = zeroNum - 1
            break
    zeroCheck = zeroCheck - 1
        
        

print(nums)
        
    
                