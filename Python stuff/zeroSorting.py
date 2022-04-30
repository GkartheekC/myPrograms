array = [1, 2, 0, 3, 0]
arrayCount = 0
zeroIndex = 0
finalList =[]


for i in range(len(array)):
    arrayCount += 1

for i in array:
    finalList.append(i)

for i in array:
    if i == 0:
        zeroPlace = array.index(i)
        zeroIndex = zeroPlace - arrayCount

        for i in range(zeroIndex, -1):
            finalList[i+1] = array[i]

            

print(finalList)