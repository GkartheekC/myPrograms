array = [1, 124, 2567, 12345, 1234]
numOfEvens = 0
checkDigits = 0
evenCheck = 0

for i in array:
    sepNum = str(i)

    for j in sepNum:
        checkDigits += 1

    evenCheck = checkDigits%2

    if evenCheck == 0:
        numOfEvens += 1
    
    checkDigits = 0

print(numOfEvens)