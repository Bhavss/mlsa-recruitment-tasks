n = int(input("Enter the length of the string: "))
k = int(input("Enter the no. of characters: "))
s = input("Enter the string: ")
glist = list(input("Enter the characters: "))
#Taking the input of the characters in the form of a list
count = 0
ans = 0
for item in s:
    if item in glist:
        count += 1
        # counting the number of continuous matching characters
    else:
        ans = ans + (count*(count + 1))/2
        # for a continuous matching string, we can get the number of substrings using this formula
        count = 0
        # resetting count at every non-matching character
ans = ans + (count*(count + 1))/2
# if the iteration continues till the last character in the string we need to add that in our answer
print(ans)
