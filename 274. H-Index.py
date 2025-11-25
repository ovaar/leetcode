"""
274. H-Index

Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.

According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h 
papers that have each been cited at least h times.

 

Example 1:

Input: citations = [3,0,6,1,5]
Output: 3
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.

Example 2:

Input: citations = [1,3,1]
Output: 1

 

Constraints:

    n == citations.length
    1 <= n <= 5000
    0 <= citations[i] <= 1000


"""

from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        if len(citations) == 1: # Only one paper with a possible citation
            return int(citations[0] != 0)

        citations.sort(reverse=True) # Sort desc for checking H-index threshold

        i = 0
        # [6,5,3,1,0]
        while i < len(citations):
            citation = citations[i] # 6
            number_of_papers = i + 1 # 1
            if number_of_papers > citation:
                return i
            i += 1
        return i


if __name__ == "__main__":
    sol = Solution()
    # Example test case
    citations = [3,0,6,1,5]
    print(sol.hIndex(citations))  # Expected output: 3