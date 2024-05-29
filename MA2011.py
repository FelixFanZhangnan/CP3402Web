# 定义一个函数来模拟称重过程
def weigh(a, b, c, d, e, f, coins):
    left = [coins[a], coins[b], coins[c]]
    right = [coins[d], coins[e], coins[f]]
    left_sum = sum(left)
    right_sum = sum(right)
    if left_sum < right_sum:
        return -1
    elif left_sum > right_sum:
        return 1
    else:
        return 0

# 定义一个函数来找出假币的位置
def find_fake_coin(coins):
    # 第一次称重
    result1 = weigh(0, 1, 2, 3, coins)
    if result1 == 0:
        # 假币在4-8中
        result2 = weigh(4, 5, 6, 7, coins)
        if result2 == 0:
            # 假币在8中
            if coins[8] < coins[4]:
                return 8
            else:
                return 9
        elif result2 == -1:
            # 假币在4-7中
            result3 = weigh(4, 5, 6, 9, coins)
            if result3 == 0:
                return 7
            elif result3 == -1:
                if coins[4] < coins[5]:
                    return 4
                else:
                    return 5
            else:
                if coins[6] < coins[9]:
                    return 6
                else:
                    return 9
        else:
            # 假币在8-9中
            result4 = weigh(8, 9, 10, 11, coins)
            if result4 == 0:
                return 11
            elif result4 == -1:
                if coins[8] < coins[9]:
                    return 8
                else:
                    return 9
            else:
                if coins[10] < coins[11]:
                    return 10
                else:
                    return 11
    elif result1 == -1:
        # 假币在0-2中
        result5 = weigh(0, 1, 4, 5, coins)
        if result5 == 0:
            return 2
        elif result5 == -1:
            if coins[0] < coins[1]:
                return 0
            else:
                return 1
        else:
            if coins[4] < coins[5]:
                return 4
            else:
                return 5
    else:
        # 假币在3中
        return 3

# 生成所有可能的硬币重量组合
# coins = [1, 1, 1, 1, 1, 1, 1, 1, 2]

# 找出所有可能的解
solutions = []
for i in range(1, 11):
    for j in range(1, 11):
        for k in range(1, 11):
            for l in range(1, 11):
                for m in range(1, 11):
                    for n in range(1, 11):
                        for o in range(1, 11):
                            for p in range(1, 11):
                                for q in range(1, 11):
                                    coins = [i, j, k, l, m, n, o, p, q]
                                    fake_coin = find_fake_coin(coins)
                                    if fake_coin is not None:
                                        solutions.append((coins, fake_coin))

# 打印所有可能的解
for solution in solutions:
    print("Coins:", solution[0], " Fake coin at position:", solution[1])