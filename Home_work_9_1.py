def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    result = {}
    
    for coin in coins:
        if amount >= coin:
            num_coins = amount // coin
            amount -= num_coins * coin
            result[coin] = num_coins
    
    return result

print(find_coins_greedy(113))  