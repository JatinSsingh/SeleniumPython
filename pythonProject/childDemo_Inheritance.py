from Oops_Concept import Calculator


class ChildDemo(Calculator):
    num2 = 50

    def __init__(self):
        Calculator.__init__(self, 1, 1)

    def getCompleteData(self):
        return self.num2 + self.num + self.number()


obj3 = ChildDemo()
print(obj3.getCompleteData())
