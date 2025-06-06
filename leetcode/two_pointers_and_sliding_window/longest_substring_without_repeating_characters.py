class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        left = 0
        right = 0
        max_size = 1
        seen = {}
        while right <= len(s) -1: 
            if s[right] in seen:
                left = max(left, seen[s[right]] + 1)
                
            seen[s[right]] = right
            right += 1
            max_size = max(max_size, right - left)
        return max_size

        
if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring("abcabcbb")) # 3
    print(Solution().lengthOfLongestSubstring("bbbbbb")) # 1
    print(Solution().lengthOfLongestSubstring("pwwkew")) # 3
        