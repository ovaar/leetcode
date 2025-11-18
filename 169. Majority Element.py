"""
169. Majority Element

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3

Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2

 

Constraints:

    n == nums.length
    1 <= n <= 5 * 104
    -109 <= nums[i] <= 109
    The input is generated such that a majority element will exist in the array.

 
Follow-up: Could you solve the problem in linear time and in O(1) space?
"""

# space complexity: O(1)       - No extra arrays needed, only a few variables
# runtime complexity: O(n)     - Single pass through the array

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        return candidate

if __name__ == "__main__":
    sol = Solution()
    print(sol.majorityElement([3,2,3]))  # Output: 3
    print(sol.majorityElement([2,2,1,1,1,2,2]))  # Output: 2
