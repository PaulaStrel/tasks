price = [0, 1, 2, 8, 3, 9, 7]

def min_cost(n, price):
    cost = [-1] * (n + 1)
    cost[0] = price[0]
    cost[1] = price[1]
    cost[2] = price[1] + price[2]
    for i in range(3, n + 1):
        cost[i] = min(cost[i - 2],cost[i-1]) + price[i]
    print(cost[-1])


min_cost(6, price)