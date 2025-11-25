"""
45. Jump Game II

You are given a 0-indexed array of integers nums of length n. You are initially positioned at index 0.

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at index i, you can jump to any index (i + j) where:

    0 <= j <= nums[i] and
    i + j < n

Return the minimum number of jumps to reach index n - 1. The test cases are generated such that you can reach index n - 1.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:

Input: nums = [2,3,0,1,4]
Output: 2

 

Constraints:

    1 <= nums.length <= 104
    0 <= nums[i] <= 1000
    It's guaranteed that you can reach nums[n - 1].


"""

from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        
        jumps = 0
        current_end = 0  # End of range for current jump level
        farthest = 0     # Farthest position reachable so far
        
        for i in range(n - 1):  # Don't need to check last position
            farthest = max(farthest, i + nums[i])
            
            if i == current_end:  # Reached end of current jump level
                jumps += 1
                current_end = farthest
                
                if current_end >= n - 1:  # Can reach the end
                    break
        
        return jumps


if __name__ == "__main__":
    s = Solution()

    nums1 = [2,3,1,1,4]
    print(s.jump(nums1)) # Output: 2

    nums2 = [2,3,0,1,4]
    print(s.jump(nums1)) # Output: 2


