class Solution:
    def isValid(self, s: str) -> bool:
        values = {
            "(": ")",
            "[": "]",
            "{": "}",
           
        }
        close = {
            "}":"{",
            "]":"[",
            ")":"(",
        }
        track = []
        for char in s:
            if close.get(char) and not track:
                return False
            if values.get(char):
                track.append(char)
            elif track.pop() != close.get(char):
                return False
        return not track

                
            

if __name__ == "__main__":
    print(Solution().isValid("{}")) # True
    print(Solution().isValid("()[]{}")) # True
    print(Solution().isValid("(]")) # False
    print(Solution().isValid("([])")) #  True