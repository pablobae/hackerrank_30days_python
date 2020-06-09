import re

if __name__ == '__main__':
    N = int(input())

    matches = []
    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]

        pattern = '^[a-z]+[\.{1}[a-z]+]*@gmail\.com$'

        if re.match(pattern, emailID):
            matches.append(firstName)

    matches.sort()
    for i in range(len(matches)):
        print(matches[i])
