class Solution:
    def isPalindrome(self, s):

        ns = ''

        for n in s:
            if n.isalnum():
                ns += n.lower()

        return ns == ns[::-1]


        