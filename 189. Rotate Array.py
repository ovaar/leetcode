"""
189. Rotate Array

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

 

Constraints:

    1 <= nums.length <= 105
    -231 <= nums[i] <= 231 - 1
    0 <= k <= 105

 

Follow up:

    Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
    Could you do it in-place with O(1) extra space?

"""

from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n

        # Solution 1: Slicing (O(n) space - creates temporary arrays)
        # nums[:] = nums[-k:] + nums[:-k]

        # Solution 2: 3-Step Reverse (O(1) space - true in-place)
        # Example: [1,2,3,4,5,6,7], k=3
        # Step 1: [7,6,5,4,3,2,1]  - reverse all
        # Step 2: [5,6,7,4,3,2,1]  - reverse first k
        # Step 3: [5,6,7,1,2,3,4]  - reverse last n-k
        
        def reverse(start: int, end: int) -> None:
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        
        reverse(0, n - 1)      # Reverse entire array
        reverse(0, k - 1)      # Reverse first k elements
        reverse(k, n - 1)      # Reverse remaining elements
        

if __name__ == "__main__":

    sol = Solution()
    nums1 = [1,2,3,4,5,6,7]
    k1 = 3
    sol.rotate(nums1, k1)
    print(nums1)  # Output: [5,6,7,1,2,3,4]