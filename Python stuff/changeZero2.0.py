arr = [1, 0, 1, 0, 1, 1]
prev = 0
currentSeq = 0
maxSeq = 0
zeroChange = 0

for i in arr:
    if i == 0:
        if prev == 0:
            currentSeq = 1
            zeroChange = 1
        
        else:
            if zeroChange == 0:
                currentSeq += 1
                zeroChange = 1
        
    else:
        currentSeq += 1
    
    if currentSeq > maxSeq:
        maxSeq = currentSeq
    
    prev = i

print(maxSeq)

            



