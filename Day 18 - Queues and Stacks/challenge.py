import sys


class Solution:

    def __init__(self):
        self.stack = []
        self.queue = []

    def pushCharacter(self, character):
        """ Add a character to the stack (Push method)"""
        self.stack.append(character)

    def popCharacter(self):
        """ Get out from the stack the last character added """
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            raise IndexError('Stack empty')

    def enqueueCharacter(self, character):
        """ Add a character to the queue """
        self.queue.append(character)

    def dequeueCharacter(self):
        """ get out from the queue the first character added"""
        if len(self.queue) > 0:
            return self.queue.pop(0)
        else:
            raise IndexError('Queue empty')


# read the string s
s = input()
# Create the Solution class object
obj = Solution()

l = len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

isPalindrome = True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
'''
for i in range(l // 2):
    if obj.popCharacter() != obj.dequeueCharacter():
        isPalindrome = False
        break
# finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, " + s + ", is a palindrome.")
else:
    print("The word, " + s + ", is not a palindrome.")
