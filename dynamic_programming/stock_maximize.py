#
class Solution:
    def maxProfit1(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        mins = [stock for stock in prices]
        maxs = [stock for stock in prices]
        mins[0] = prices[0]
        maxs[-1] = prices[-1]

        for i in range(1, len(prices)):
            mins[i] = min(mins[i - 1], prices[i - 1])
        for i in range(len(prices)-2, -1, -1):
            maxs[i] = max(maxs[i + 1], prices[i + 1])

        max_profit = 0
        for i in range(len(prices)):
            if maxs[i] - mins[i] > max_profit:
                max_profit = maxs[i] - mins[i]

        return max_profit

    def maxProfit(self, prices):
        min_price = float('inf')
        max_profit = 0

        for i in range(len(prices)):
            min_price = min(min_price, prices[i])
            if prices[i]-min_price > max_profit:
                max_profit = prices[i] - min_price

        return max_profit

s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))
print(s.maxProfit([7,7,7]))
print(s.maxProfit([7,2,17]))
print(s.maxProfit([3,2,6,5,0,3]))

