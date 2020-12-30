"""
You are given the prices of a stock, in the form of an array of integers, prices. 
Let's say that prices[i] is the price of the stock on the ith day (0-based index). 
Assuming that you are allowed to buy and sell the stock only once, 
your task is to find the maximum possible profit (the difference between the buy and sell prices).

Note: You can assume there are no fees associated with buying or selling the stock.

Example

For prices = [6, 3, 1, 2, 5, 4], the output should be buyAndSellStock(prices) = 4.

It would be most profitable to buy the stock on day 2 and sell it on day 4. 
Thus, the maximum profit is prices[4] - prices[2] = 5 - 1 = 4.

For prices = [8, 5, 3, 1], the output should be buyAndSellStock(prices) = 0.

Since the value of the stock drops each day, 
there's no way to make a profit from selling it. Hence, the maximum profit is 0.

For prices = [3, 100, 1, 97], the output should be buyAndSellStock(prices) = 97.

It would be most profitable to buy the stock on day 0 and sell it on day 1. 
Thus, the maximum profit is prices[1] - prices[0] = 100 - 3 = 97.

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer prices

Guaranteed constraints:
1 ≤ prices.length ≤ 105,
1 ≤ prices[i] ≤ 106.

[output] integer

The maximum possible profit.
"""

"""https://www.youtube.com/watch?v=PV97reU3Vig"""


"""Brute Force Solution"""

# def buyAndSellStock(prices):
#     max_profit = 0
#     for i in range(len(prices)):
#         for j in range(i+1, len(prices)):
#             profit = prices[j] - prices[i]
#             if profit > max_profit:
#                 max_profit = profit
#     return max_profit




def buyAndSellStock(prices):
    max_profit = 0
    # put a large value here and replace as you find a smaller one
    smallest = prices[0]
    
    for i in range(1, len(prices)):
        
        # check if the 
        if prices[i] < smallest:
            smallest = prices[i]
            
        elif (prices[i] - smallest) > max_profit:
                max_profit = prices[i] - smallest

        
            
    return max_profit
    

            
prices = [6, 3, 1, 2, 5, 4]
print(buyAndSellStock(prices)) # = 4.
prices = [8, 5, 3, 1]
print(buyAndSellStock(prices)) # = 0.
prices = [3, 100, 1, 97]
print(buyAndSellStock(prices)) # = 97.



reasoning = """
1. In order to get the Max Profit,
we need the numbers that are furthest apart.
Let us look for the lowest price.

2. then we need the largest price after the lowest price 
in order to make a MAX_PROFIT

3. Compare with other profits and return MAX_PROFIT
"""

print(reasoning)