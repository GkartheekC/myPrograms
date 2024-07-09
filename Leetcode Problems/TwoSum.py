## Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.


## Variables
#Setting up an array
array = [2, 7, 11, 15]

#Setting up a target sum
targetSum = 9

#Setting up array to return two correct indices
indexArray = []

#Setting up a variable to hold current number in array in order to compare to other numbers in the array
currentNum = 0

## Logic
#Setting up a for loop to go through the entire array
for i in range(0, len(array)):

    #Setting the value of currentNum to the index in the array that the for loop is currently on
    currentNum = array[i]

    #Setting up for loop to check currentNum with other numbers in the array
    for j in range(i+1, len(array)):

        #Checking if value of currentNum and new value taken from array using variable j is equal to targetSum
        if currentNum + array[j] == targetSum:

            #Appending correct indexes to indexArray if they equal targetSum
            indexArray.append(i)
            indexArray.append(j)   

#Printing to see if code works
print(indexArray)  
