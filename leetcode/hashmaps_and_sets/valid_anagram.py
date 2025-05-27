
def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if len(s) != len(t):
        return False
    letters = {}
    for letter in s:
        if letter not in letters:
            letters[letter] = 1
        else:
            letters[letter] += 1
    for letter in t:
        if letter in letters:
            letters[letter]-=1
            if letters[letter] == 0:
                del letters[letter]
        
    return len(letters) == 0


if __name__ == "__main__":
    # expecte value [["bat"],["nat","tan"],["ate","eat","tea"]]
    print(isAnagram("anagram", "nagaram"))

