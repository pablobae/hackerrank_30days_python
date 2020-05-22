#!/bin/python3

if __name__ == '__main__':
    n = int(input())

    num_max_consecutive_ones = 0
    num_consecutive_ones = 0
    while n >= 2:
        binary_digit = n % 2
        if binary_digit == 1:
            num_consecutive_ones += 1
        else:
            if num_consecutive_ones > num_max_consecutive_ones:
                num_max_consecutive_ones = num_consecutive_ones
            num_consecutive_ones = 0
        n = n // 2

    if n == 1:
        num_consecutive_ones += 1
        if num_consecutive_ones > num_max_consecutive_ones:
            num_max_consecutive_ones = num_consecutive_ones

    print(num_max_consecutive_ones)
