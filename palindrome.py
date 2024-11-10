class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            left_is_valid = (s[l].isalpha() or s[l].isnumeric())
            right_is_valid = (s[r].isalpha() or s[r].isnumeric())
            if left_is_valid and right_is_valid:
                if s[l].lower() != s[r].lower():
                    return False
                l += 1
                r -= 1
            elif left_is_valid:
                r -= 1
            elif right_is_valid:
                l += 1
            else:
                l += 1
                r -= 1
        
        return True
