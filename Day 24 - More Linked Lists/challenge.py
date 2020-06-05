class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def insert(self, head, data):
        p = Node(data)
        if head == None:
            head = p
        elif head.next == None:
            head.next = p
        else:
            start = head
            while (start.next != None):
                start = start.next
            start.next = p
        return head

    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def removeDuplicates(self, head):
        values = []
        if head == None:
            return head
        else:
            start = head
            previous_node = None
            while start is not None:
                if not start.data in values:
                    values.append(start.data)
                    previous_node = start
                else:
                    if start.next is not None:
                        previous_node.next = start.next
                    else:
                        previous_node.next = None
                start = start.next

        return head


mylist = Solution()
T = int(input())
head = None
for i in range(T):
    data = int(input())
    head = mylist.insert(head, data)
head = mylist.removeDuplicates(head)
mylist.display(head)
