# prices = [7, 1, 5, 3, 6, 4]
prices = [ 2, 4, 1]
left = 0
right = 1
maxP = 0
while right < len(prices):
    if prices[left] < prices[right]:
        profit = prices[right] - prices[left]
        maxP = max(maxP, profit)
    else:
        left = right
    right += 1
print(maxP)