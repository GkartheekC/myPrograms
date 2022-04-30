array = ["h", "e", "l", "l", "o"]
reversedArray = []

length = len(array)

for i in range(len(array)):
    reversedArray.append(array[length - i-1])
    

print(reversedArray)