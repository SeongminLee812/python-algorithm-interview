from typing import *
import sys
def maxProfit(prices: List[int]) -> int:
    max_price = 0

    for i in range(0, len(prices) - 1):
        for j in range(i + 1, len(prices)):
            max_price = max(max_price, prices[j] - prices[i])

    return max_price

def maxProfit(prices: List[int]) -> int:
    profit = 0
    min_price = sys.maxsize

    for price in prices:
        min_price = min(min_price, price)
        profit = max(profit, price - min_price)

    return profit