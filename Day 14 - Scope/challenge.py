class Difference:
    def __init__(self, a):
        self.__elements = a

    # Add your code here
    def computeDifference(self):
        sorted_elements = self.__elements.copy()
        sorted_elements.sort()
        self.maximumDifference = sorted_elements[len(sorted_elements) - 1] - sorted_elements[0]
        # End of Difference class
