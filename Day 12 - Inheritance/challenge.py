class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
    def __init__(self, firstName, lastName, id, scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = id
        self.scores = scores

    def calculate(self):
        sum_score = 0
        for score in self.scores:
            sum_score += score

        average = sum_score/len(self.scores)

        grade = ''
        if average < 40:
            grade = 'T'
        elif 40 <= average < 55:
            grade = 'D'
        elif 55 <= average < 70:
            grade = 'P'
        elif 70 <= average < 80:
            grade = 'A'
        elif 80 <= average < 90:
            grade = 'E'
        else:
            grade = 'O'

        return grade


line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input())  # not needed for Python
scores = list(map(int, input().split()))
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())

