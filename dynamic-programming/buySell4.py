class Solution:
    def __init__(self):
        self.cache = {}
        
    def maxProfit(self, k: int, prices: List[int]) -> int:
        return self.maxStockProfit(prices, canBuy=True, transactions=k, currentIndex=0)
    
    def maxStockProfit(self, prices, canBuy, transactions, currentIndex):
        if currentIndex >= len(prices) or transactions < 1:
            return 0
        
        currentKey = (canBuy, transactions, currentIndex)
        
        if currentKey in self.cache:
            return self.cache[currentKey]
        
        if canBuy:
            buy = self.maxStockProfit(prices, not canBuy, transactions, currentIndex + 1) - prices[currentIndex]
            idle = self.maxStockProfit(prices, canBuy, transactions, currentIndex + 1)
            
            self.cache[currentKey] = max(buy, idle)
        else:
            sell = self.maxStockProfit(prices, not canBuy, transactions - 1, currentIndex + 1) + prices[currentIndex]
            idle = self.maxStockProfit(prices, canBuy, transactions, currentIndex + 1)
            
            self.cache[currentKey] = max(sell, idle)
        
        return self.cache[currentKey]