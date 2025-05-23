class Solution:
    def is_palindrome(self, x: int) -> bool:
        initial = str(x)
        reverse = str(x) [::-1]
        if initial == reverse:
            return True
        return False
    
solution = Solution()
solution.is_palindrome(12121)
solution.is_palindrome(-12121)
solution.is_palindrome(10)
