class Recursion:
    def main(self):
        self.print1(1)

    def print1(self, n):
        print(n)
        self.print2(2)

    def print2(self, n):
        print(n)
        self.print3(3)

    def print3(self, n):
        print(n)
        self.print4(4)

    def print4(self, n):
        print(n)
        self.print5(5)

    def print5(self, n):
        print(n)


a = Recursion()
a.main()