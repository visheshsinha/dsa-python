class Solution:
    def __init__(self) -> None:
        self.cache = {}

    def maxProfit(self, prices: List[int], fee: int) -> int:
        return self.stockProfit(prices, currentDay=0, flag=True, transaction=fee)

    def stockProfit(
        self, prices: List[int], currentDay: int, flag: bool, transaction: int
    ) -> int:

        if currentDay >= len(prices):
            return 0

        currentKey = (currentDay, flag)

        if currentKey in self.cache:
            return self.cache[currentKey]

        if flag:

            idle = self.stockProfit(prices, currentDay + 1, flag, transaction)
            buy = (
                self.stockProfit(prices, currentDay + 1, not flag, transaction)
                - prices[currentDay]
            )
            self.cache[currentKey] = max(idle, buy)
            return self.cache[currentKey]

        else:

            idle = self.stockProfit(prices, currentDay + 1, flag, transaction)
            sell = (
                self.stockProfit(prices, currentDay + 1, not flag, transaction)
                + prices[currentDay] - transaction
            )
            self.cache[currentKey] = max(idle, sell)
            return self.cache[currentKey]
