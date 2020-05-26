# Write a program that takes an array denoting the daily stock price, 
# and retums the maximum profit that could be made by buying 
# and then selling one share of that stock. 
# There is no need to buy if no profit is possible.
# Hint:ldentifying the minimum and maximum is not enough 
# since the minimum may appear after the maximum height. 
# Focus on valid differences.

def buy_and_sell_stock_once(prices):
    max_profit_so_far, min_price_so_far = 0, prices[0]
    
    for price in prices[1:]:
        min_price_so_far = min(min_price_so_far, price)
        max_profit = price - min_price_so_far 
        max_profit_so_far = max(max_profit_so_far, max_profit)
            
    return max_profit
