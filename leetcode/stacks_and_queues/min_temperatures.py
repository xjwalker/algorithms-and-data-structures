from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                res[prev_index] = i - prev_index
            stack.append(i)
        return res

if __name__ == "__main__":
    print(Solution().dailyTemperatures([73,74,75,71,69,72,76,73])) # [1,1,4,2,1,1,0,0]
    print(Solution().dailyTemperatures([30,40,50,60])) # [1,1,1,0]
    print(Solution().dailyTemperatures([30,60,90])) # [1,1,0]

        