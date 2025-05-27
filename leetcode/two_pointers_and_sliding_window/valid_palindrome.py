class Solution:

    def isPalindrome(self, s: str) -> bool:
        f = "".join([char.lower() for char in s if char.isalnum()])
        return f == f[::-1]
    
if __name__ == "__main__":
    print(Solution().isPalindrome("A man, a plan, a canal: Panama"))    #True
    print(Solution().isPalindrome("race a car"))  # False
    print(Solution().isPalindrome(" "))   # true