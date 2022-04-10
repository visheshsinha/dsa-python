class Solution:
    def __init__(self):
        self.cache = {}
        
    def maxProfit(self, prices: List[int]) -> int:
        return self.maxStockProfit(prices, canBuy=True, currentIndex=0)
    
    def maxStockProfit(self, prices, canBuy, currentIndex):
        if currentIndex >= len(prices):
            return 0
        
        currentKey = (canBuy, currentIndex)
        
        if currentKey in self.cache:
            return self.cache[currentKey]
        
        if canBuy:
            buy = self.maxStockProfit(prices, not canBuy, currentIndex + 1) - prices[currentIndex]
            idle = self.maxStockProfit(prices, canBuy, currentIndex + 1)
            
            self.cache[currentKey] = max(buy, idle)
        else:
            sell = self.maxStockProfit(prices, not canBuy, currentIndex + 2) + prices[currentIndex]
            idle = self.maxStockProfit(prices, canBuy, currentIndex + 1)
            
            self.cache[currentKey] = max(sell, idle)
        
        return self.cache[currentKey]