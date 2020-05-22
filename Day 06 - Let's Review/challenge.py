# Enter your code here. Read input from STDIN. Print output to STDOUT
num_cases = int(input())
for case in range(num_cases):
    S = input()
    evenS = S[::2]
    oddS = S[1::2]
    print(evenS + " " + oddS)
