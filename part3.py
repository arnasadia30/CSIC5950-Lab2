#!/usr/bin/python
# p1q2

# When are tickets most likely to be issued?

from __future__ import print_function
import pyspark
from pyspark import SparkContext

# reload(sys)
# sys.setdefaultencoding('utf8')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: part3.py <file>", file=sys.stderr)
        sys.exit(-1)

sc = SparkContext()

data = sc.textFile("ticket_data.csv")

header = data.first()

data = data.filter(lambda line: line != header)

tickets = data.map(lambda line: (line.split(",")[3], 1))

counts = tickets.reduceByKey(lambda a, b: a + b)

filtered = counts.filter(lambda x: x[1] > 10)

sorted = filtered.sortBy(lambda x: x[1], ascending=False)

for item in sorted.collect():
    print(item[0], item[1])
