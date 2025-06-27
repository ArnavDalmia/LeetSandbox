
def maxProfitFunctionality(prices):
    if not prices:
        return 0
        
    minPrice = prices[0]
    maxProfit = 0

    for i in prices[1:]:
        if i < minPrice:
            minPrice = i
        
        profit = i - minPrice
        maxProfit = max(maxProfit, profit)
    return maxProfit

def main(prices):
    result = maxProfitFunctionality(prices)
    
    output = f"""Stock prices: {prices}
Maximum profit: {result}"""
    
    if result > 0:
        output += f"\nBest strategy: Buy low, sell high for ${result} profit"
    else:
        output += "\nNo profit possible with this price sequence"
    
    return output

# EXAMPLE
# main([7, 1, 5, 3, 6, 4])
# main([7, 6, 4, 3, 1])
