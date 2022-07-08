# Whiteboard Question of the Day
# Find Palindrome
# Given a string of lowercase letters, write a function to see if the word is a palindrome (the same word spelled forward and backwards).
# Example Input: ‘racecar’
# Example Output: True

def palindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False

print(palindrome("ice cream"))

# instructor's answer to whiteboard
def palindrome2(word):
    left = 0
    right = len(word)-1
    while left < right:
        if word[left] != word[right]:
            return False
        left += 1
        right -= 1
    return True

print(palindrome2('applesbee'))

