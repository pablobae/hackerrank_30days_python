class Sorter:

    def __init__(self, n, a):
        self.n = n
        self.a = a
        self.num_swaps = 0

    def order(self):
        for i in range(0, self.n):
            swap_done = False
            for j in range(0, self.n - 1):
                if self.a[j] > self.a[j + 1]:
                    temp = self.a[j]
                    self.a[j] = self.a[j + 1]
                    self.a[j + 1] = temp
                    self.num_swaps += 1
                    swap_done = True
            if not swap_done:
                break

    def swaps(self):
        return self.num_swaps

    def first_element(self):
        return self.a[0]

    def last_element(self):
        return self.a[self.n - 1]


n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

sorter = Sorter(n, a)
sorter.order()
print(f'Array is sorted in {sorter.swaps()} swaps.')
print(f'First Element: {sorter.first_element()}')
print(f'Last Element: {sorter.last_element()}')
