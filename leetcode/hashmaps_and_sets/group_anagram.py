def quicksort_string(s):
    if len(s) <= 1:
        return s
    pivot = s[len(s) // 2]
    left = [x for x in s if x < pivot]
    middle = [x for x in s if x == pivot]
    right = [x for x in s if x > pivot]
    return quicksort_string(left) + middle + quicksort_string(right)

def sort_strings_in_array(arr):
    return [quicksort_string(s) for s in arr]

def groupAnagrams(strs: list[str]) -> list[list[str]]:
    words_dict = {}
    for word in strs:
        sorted_word = "".join(sorted(word))
        if sorted_word in words_dict:
            words_dict[sorted_word].append(word)
        else:
            words_dict[sorted_word] = [word]
    result=[]
    for key, words in words_dict.items():
        result.append(words_dict[key])
    return result

if __name__ == "__main__":
    # expecte value [["bat"],["nat","tan"],["ate","eat","tea"]]
    print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))