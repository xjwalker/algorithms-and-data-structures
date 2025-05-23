def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    max_price = -1
    max_diff = 0
    min_price = float("Inf")
    for price in prices:
        if price < min_price: # 4 < 2
            min_price = price # 2 
            max_price = price     # 2
            max_diff = max(max_diff, price - min_price)
        
        if price > max_price:  # 4 > 2
            max_diff = max(max_diff, price - min_price) 
            max_price = price   # 4
    
    if max_price == -1:
        return 0

    return max_diff

if __name__ == "__main__":
    # expecte value 5
    print(maxProfit([7,1,5,3,6,4]))