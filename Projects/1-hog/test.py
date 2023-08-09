def count_partitions(n, dice_num):
    if n == 0 and dice_num == 0:
        return 1
    elif n < 0:
        return 0
    elif dice_num == 0:
        return 0
    else:
        summation = 0
        for i in range(1, 7):
            summation += count_partitions(n - i, dice_num - 1)
        return summation


def probability(upper_bond, lower_bond, dice_num):
    def p_helper(x):
        return count_partitions(x, dice_num) / (6 ** dice_num)

    max_range = 6 ** dice_num
    i, j, first_total, second_total = 0, 0, 0, 0

    if lower_bond != -1:
        while (lower_bond + 10 * i) < max_range:
            first_total += p_helper(lower_bond + 10 * i)
            i += 1

    if upper_bond != -1:
        while (upper_bond + 10 * j) < max_range:
            second_total += p_helper(upper_bond + 10 * j)
            j += 1

    return first_total + second_total


def current_prob(my_bit, ten_bit, one_bit, dice_num):
    lower_bond, upper_bond = -1, -1

    if 0 <= one_bit - ten_bit <= 9:
        if 0 <= my_bit < one_bit - ten_bit:
            lower_bond = one_bit - ten_bit - my_bit

        elif one_bit - ten_bit <= my_bit <= 9:
            lower_bond = one_bit - ten_bit - my_bit + 10

    # be aware of the case when ten_bit is 0
    if ten_bit != 0 <= one_bit + ten_bit <= 9:
        if 0 <= my_bit < one_bit + ten_bit:
            upper_bond = one_bit + ten_bit - my_bit

        elif one_bit + ten_bit <= my_bit <= 9:
            upper_bond = one_bit + ten_bit - my_bit + 10

    return probability(upper_bond, lower_bond, dice_num)


def dice_one_prob(dice_num):
    if dice_num == 0:
        return 0
    else:
        return 1 / 6 + 5 / 6 * dice_one_prob(dice_num - 1)


def temp_test():
    # dice_num = 4
    # nope = dice_one_prob(dice_num)
    # print(nope)
    for dice_num in range(1, 6):
        nope = dice_one_prob(dice_num)
        print(nope)

        # for my_bit in range(10):
        #     for ten_bit in range(10):
        #         for one_bit in range(10):
        #             p = current_prob(my_bit, ten_bit, one_bit, dice_num)
        #
        #             # if current_prob(my_bit, ten_bit, one_bit, dice_num) > 0.2:
        #             # print(dice_num, "|", my_bit, "|", ten_bit, one_bit, p)
        #

temp_test()
