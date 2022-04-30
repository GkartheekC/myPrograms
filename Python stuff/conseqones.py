array = [1, 0, 1, 1, 1, 1, 0, 1, 1]
numOfConseq = 0
maxOnes = 0

for i in array:
    if i == 1:
        numOfConseq += 1
    
    else:
        numOfConseq = 0
    
    if numOfConseq > maxOnes:
        maxOnes = numOfConseq
        
    

print(maxOnes)
