#!/bin/python3


if __name__ == '__main__':
    N = int(input())

    output = ''
    if N % 2 == 1:
        output = 'Weird'
    elif 2 <= N <= 5:
        output = 'Not Weird'
    elif 6 <= N <= 20:
        output = 'Weird'
    elif N > 20:
        output = 'Not Weird'
    else:
        output = ''
