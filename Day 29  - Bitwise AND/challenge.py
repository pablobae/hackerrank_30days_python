def maximum(number, k):
    max_value = 0
    for a in range(1, number):

        b = a + 1
        while b <= number:
            bitwise_and_value = a & b
            if bitwise_and_value < k and bitwise_and_value > max_value:
                max_value = bitwise_and_value
            b += 1

    return max_value


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])
        print(maximum(n, k))
