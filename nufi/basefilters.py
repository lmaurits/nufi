class Summer:

    def __init__(self):

        self.total = 0

    def process(self, number):

        self.total += number

class Counter:

    def __init__(self):

        self.count = 0

    def process(self, number):

        self.count += 1

class Collector:

    def __init__(self):
        
        self.values = []

    def process(self, number):

        self.values.append(number)
