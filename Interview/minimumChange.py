def minChange(coinsArr, value):
    # coins are coins available = [25,10,5,1]

    # for this round 25 is the coins arr[0]
    change = value
    # while (change > 0):
    change = change % coinsArr[0]
    if change == 0:
        coin = value / coinsArr[0]
    else:
        coin = 10000000
        # calculate the floor and the remainder for next round
        # coins += floor
        # remainder for next round
    return coin
    # next the value is reduced coins * 25

print(minChange([25,10,5,1], 50))
        