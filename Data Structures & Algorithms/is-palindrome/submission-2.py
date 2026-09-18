class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            # Use isalnum() for checking
            while l < r and not s[l].isalnum():
                l += 1
            while r > l and not s[r].isalnum():
                r -= 1

            # Comparison remains the same
            if s[l].lower() != s[r].lower():
                return False

            # Pointer movement remains the same
            l, r = l + 1, r - 1

        return True