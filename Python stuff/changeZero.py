array = [1]
one = 0
zero = 0
conseqOnes = []
conseqZeros = []
prev = 2
loopCount = 0
changeZero = []
maxOnes = 0



for i in array:

    loopCount += 1

    if i == 1 :
        if prev == 0:
            one = 1
            conseqZeros.append(zero)
            prev = 1
        
        else:
            one += 1
            prev = 1
        
        if loopCount == len(array):
            conseqOnes.append(one)
    
    else:
        if prev == 1:
            zero = 1
            conseqOnes.append(one)
            prev = 0
        
        else:
            zero += 1
            prev = 0
        
        if loopCount == len(array):
            conseqZeros.append(zero)


if array[0] == 1:
     if len(conseqZeros) < len(conseqOnes):
         conseqZeros.append(1)
    
if array[0] == 0:
     if len(conseqOnes) < len(conseqZeros):
        conseqZeros.pop(0)

for i in range(len(conseqOnes)):
    
    if len(conseqOnes) > 1:

        if i < len(conseqOnes) - 1:
            if conseqZeros[i] == 1:
                maxOnes = conseqOnes[i] + conseqOnes[i + 1] + 1

            else:
                maxOnes = conseqOnes[i] + 1

        else:
            maxOnes = conseqOnes[i] + 1
        
    else:
        maxOnes = conseqOnes[i] + 1

    changeZero.append(maxOnes)

for i in changeZero:
    if i > maxOnes:
        maxOnes = i

print(maxOnes)





