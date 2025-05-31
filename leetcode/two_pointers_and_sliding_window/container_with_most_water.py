class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) -1
        max_calc = 0
        while left < right:
            distance = right - left
            min_val = min(height[left], height[right])
            calc = min_val * distance 
            max_calc = max(calc, max_calc)
            # print(f"{min_val} from {left} to {right} distance is {distance} * min = {calc}")
            if height[left] > height[right]:
                right -=1
            elif height[right] >= height[left]: 
                left += 1
            
            
        return max_calc


if __name__ == "__main__":
    print(Solution().maxArea([1,2,1])) # 2
    print(Solution().maxArea([4,3,2,1,4])) # 16
    print(Solution().maxArea([1,1]))   # 1
    print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))   # 49
