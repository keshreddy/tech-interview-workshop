from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n

        # Calculate the product of all elements to the left of each index
        multnum = 1
        for i in range(n):
            answer[i] = multnum  # Store the running product so far
            multnum *= nums[i]  # Update multnum with nums[i]
        
        # Calculate the product of all elements to the right of each index
        multnum = 1
        for i in range(n - 1, -1, -1):  # Traverse from the end
            answer[i] *= multnum  # Multiply the existing left product by the right product
            multnum *= nums[i]  # Update multnum with nums[i]

        return answer
