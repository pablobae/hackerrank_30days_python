import sys

num_contacts = int(input())
phone_book = {}
for _ in range(num_contacts):
    contacts_raw = input().split(" ")
    phone_book.update({contacts_raw[0]: contacts_raw[1]})

lines_queries = sys.stdin.readlines()
for line in lines_queries:
    name = line.strip()
    if name == "":
        break
    else:
        if name in phone_book:
            print(name + "=" + phone_book[name])
        else:
            print("Not found")
