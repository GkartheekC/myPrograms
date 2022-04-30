array = [3,2,1]
mountain = True
check = 0
prev = 0
loopCount = 0
positiveNum = 0
negative = 0
positive = True

if len(array)<3:
    mountain = False

for i in array:
    check = i - prev
    prev = i

    if check > 0:
        if (not positive):
            mountain = False
    
    if check < 0:
        if loopCount > 1:
            negative = negative + 1
            positive = False
        
        else:
            mountain = False
    
    if loopCount > 0:
        if check == 0:
            mountain = False
    
    loopCount = loopCount + 1

if negative == 0:
    mountain = False

print(mountain)

