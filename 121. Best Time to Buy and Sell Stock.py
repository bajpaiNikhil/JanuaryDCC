

def maxProfit(prices):

    # aPrices = prices.sort()
    # bPrices = prices.sort(reverse=True)

    low = prices[0]
    profit = 0

    #
    # if prices == aPrices:
    #     return prices[-1]-prices[0]
    # if prices == bPrices:
    #     return 0

    for i in range(1, len(prices)):
        low = min(prices[i] , low)
        print(low)
        profit = max( profit , prices[i] - low)
    return profit


prices = [7,6,4,3,1]
print(maxProfit(prices))
