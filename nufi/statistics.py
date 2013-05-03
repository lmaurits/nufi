
from nufi.basefilters import Collector

class Median(Collector):
    
    def output(self):

        import scipy.stats
        print scipy.stats.scoreatpercentile(self.values, 50)

class Mode(Collector):
    
    def output(self):

        import scipy.stats
        print float(scipy.stats.mode(self.values, axis=None)[0])

class Summary(Collector):

    def output(self):

        import scipy.stats
        print "Min: ", min(self.values)
        print "Lower quartile: ", scipy.stats.scoreatpercentile(self.values, 25)
        print "Median: ", scipy.stats.scoreatpercentile(self.values, 50)
        print "Upper quartile: ", scipy.stats.scoreatpercentile(self.values, 75)
        print "Max: ", max(self.values)

