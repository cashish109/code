
def isPalindrom(data):
    if(data.casefold().__eq__("".join(reversed(data.casefold())))):
        return True
    else:
        return False


data = input("Input value: ")
if(isPalindrom(data)):
    print("Palindrome")
else:
    print("Not Palindrome")



