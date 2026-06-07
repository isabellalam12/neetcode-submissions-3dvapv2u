class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #input: prices (array)
        #output: profit (final price - initial price)
        #goal: maximize profit, minimize price
        #edge case: negative profit (return 0)

        max_profit = 0 
        mini_price = prices[0]

        for p in prices:
            max_profit = max(max_profit, p -mini_price)
            mini_price = min(mini_price, p)
        return max_profit

        