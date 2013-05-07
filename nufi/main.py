# Copyright (c) 2013, Luke Maurits <luke@maurits.id.au>
# Published under the terms of the BSD 3-Clause License
# (see LICENSE file or http://opensource.org/licenses/BSD-3-Clause)

from optparse import OptionParser
import sys
import nufi.basics, nufi.statistics

__version__ = "20130506a"

def main():

    parser = OptionParser()
    (options, args) = parser.parse_args()

    process = args[0]

    if process == "max":
        consumer = nufi.basics.Max()
    elif process == "mean":
        consumer = nufi.basics.Mean()
    elif process == "median":
        consumer = nufi.statistics.Median()
    elif process == "min":
        consumer = nufi.basics.Min()
    elif process == "mode":
        consumer = nufi.statistics.Mode()
    elif process == "sum":
        consumer = nufi.basics.Sum()
    elif process == "summary":
        consumer = nufi.statistics.Summary()
    else:
        print "Unknown process: %s" % process
        sys.exit(1)

    for line in sys.stdin:
        consumer.process(float(line.strip()))
    consumer.output()
