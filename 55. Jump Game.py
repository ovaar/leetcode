"""
55. Jump Game

You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

 

Constraints:

    1 <= nums.length <= 104
    0 <= nums[i] <= 105


"""

from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0

        for i in range(len(nums)):
            if i > max_reach: # Cannot reach this position :(
                return False

            max_reach = max(max_reach, i + nums[i])

            # Early exit: if we can already reach the last index, no need to continue
            if max_reach >= len(nums) - 1:
                return True
            
        # If we've checked all positions and haven't returned False, we can reach the end
        return True
        

if __name__ == "__main__":
    sol = Solution()
    # Example 1
    nums1 = [2,3,1,1,4]
    print(sol.canJump(nums1))  # Output: true

    # Example 2
    nums2 = [3,2,1,0,4]
    print(sol.canJump(nums2))  # Output: false