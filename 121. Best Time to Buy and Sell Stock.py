"""
121. Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

 

Constraints:

    1 <= prices.length <= 105
    0 <= prices[i] <= 104

"""


from typing import List
import sys
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price= sys.maxsize
        max_profit = 0

        for price in prices:
            min_price = min(min_price, price) # track lowest buy option
            max_profit = max(max_profit, price - min_price) # best profit
        
        return max_profit



if __name__ == "__main__":
    sol = Solution()
    # Example 1
    prices1 = [7,1,5,3,6,4]
    print(sol.maxProfit(prices1))  # Output: 5

    # Example 2
    prices2 = [7,6,4,3,1]
    print(sol.maxProfit(prices2))  # Output: 0

    prices3 = [1,2]
    print(sol.maxProfit(prices3))  # Output: 1