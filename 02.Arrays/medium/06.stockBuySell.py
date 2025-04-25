def stockBuySell(prices):

    max_price = 0
    min_price = float('inf')
    
    # for i in range(len(prices)):
    #     for j in range(i, len(prices)):
    #         if prices[j] > prices[i]:
    #             diff = prices[j] - prices[i]
    #             max_price = max(diff, max_price)
    
    for i in range(len(prices)-1):
        min_price = min(min_price, prices[i])
        diff = prices[i] - min_price
        max_price = max(diff, max_price)

    return max_price

prices = [7,1,5,3,6,4]
print(stockBuySell(prices))