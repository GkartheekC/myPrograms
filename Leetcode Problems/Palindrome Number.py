##Given an integer x, return true if x is a palindrome, and false otherwise.

#Variables
#Setting up variable x
x = -121

#Setting up variable to determine if number is a palindrome
palindrome = True

#Setting up for loop to check if number is a palindrome
for i in range(0, int(((len(str(x)))/2)+1)):
    if str(x)[i] != str(x)[len(str(x))-1-i]:
        palindrome = False

print(palindrome)


