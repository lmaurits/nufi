from nufi.basefilters import Summer, Counter

class Mean(Summer, Counter):

    def __init__(self):

        Summer.__init__(self)
        Counter.__init__(self)
        
    def process(self, number):

        Summer.process(self, number)
        Counter.process(self, number)

    def output(self):

        print float(self.total) / self.count

class Sum(Summer):

    def __init__(self):

        Summer.__init__(self)

    def process(self, number):

        Summer.process(self, number)

    def output(self):

        print self.total

class Min:

    def __init__(self):

        self.minimum = 0
        self.first = True

    def process(self, number):

        if self.first or number < self.minimum:
            self.minimum = number
        if self.first:
            self.first = False

    def output(self):

        print self.minimum

class Max:

    def __init__(self):

        self.maximum = 0
        self.first = True

    def process(self, number):

        if self.first or number > self.maximum:
            self.maximum = number
        if self.first:
            self.first = False

    def output(self):

        print self.maximum


