def knapsack_recursive(wt, val, n, W):

    # No items or no capacity
    if n == 0 or W == 0:
        return 0

    # If current item's weight is greater than capacity,
    # we cannot take it.
    if wt[n - 1] > W:
        return knapsack_recursive(wt, val, n - 1, W)

    #Two choices:
    # 1. Don't take the item
    # 2. Take the item
    return max(
        knapsack_recursive(wt, val, n - 1, W),
        val[n - 1] + knapsack_recursive(
            wt, val, n - 1, W - wt[n - 1]
        )
    )


wt = [2,3,4,1]
val = [3,4,5,1]
W = 5

n = len(wt)

print(knapsack_recursive(wt, val, n, W))
