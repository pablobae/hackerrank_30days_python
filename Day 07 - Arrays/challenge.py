#!/bin/python3


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    arr.reverse()
    output = ''
    add_space = False
    for item in arr:
        if add_space:
            output += ' '
        else:
            add_space = True
        output += str(item)
    print(output)
