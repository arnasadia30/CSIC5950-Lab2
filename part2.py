from __future__ import print_function
import sys
import math
from math import sqrt
from collections import Counter
from collections import defaultdict
from operator import itemgetter
from pyspark.sql import SparkSession

# reload(sys)
# sys.setdefaultencoding('utf8')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: part2.py <file>", file=sys.stderr)
        sys.exit(-1)


def closestCenter(data, center):
    distList = []
    for c in center:
        val = 0
        for j in range(3):
            val += (data[j] - c[j]) ** 2
        dist = sqrt(val)
        distList.append(dist)
    closest = float('inf')
    index = -1
    for j, h in enumerate(distList):
        if h < closest:
            closest = h
            index = j
    return int(index), data


def calculateCentroid(data):
    key, value = data[0], data[1]
    n = len(value)
    update = [0] * 3
    for j in value:
        update[0] += float(j[0])
        update[1] += float(j[1])
        update[2] += float(j[2])
    nCenter = [round(x / n, 4) for x in update]
    return nCenter


spark = SparkSession.builder.appName("part2Bonus").getOrCreate()

dataset = spark.read.format("csv").load(sys.argv[1])

dictClr = ['Black', 'BLK', 'BK.', 'B LAC', 'BLK.', 'BK', 'BLAC', 'BCK', 'BC', 'BK/']
black = dataset.filter(dataset['VC'].isin(dictClr))
dataPoints = black.select(black['Street Code1'], black['Street Code2'], black['Street Code3']).na.drop()
dRDD = dataPoints.rdd.map(lambda r: (r[0], r[1], r[2]))


ct = 4
centroidN = dRDD.takeSample(False, ct)

ctr = 0
centroidO = centroidN

for m in range(40):
    map1 = dRDD.map(lambda r: closestCenter(r, centroidO))
    reduce1 = map1.groupByKey()
    map2 = reduce1.map(lambda x: calculateCentroid(x)).collect()
    newCentroid = map2
    converge = 0
    for i in range(k):
        if newCentroid[i] == centroidO[i]:
            converge += 1
        else:
            diff = 0.0009
            closeDiff = [round((a - b) ** 2, 6) for a, b in zip(newCentroid[i], centroidO[i])]
            if all(v <= diff for v in closeDiff):
                converge += 1
    if converge >= 4:
        print(ctr)
        print(newCentroid)
        break
    else:
        ctr += 1
        print(ctr)
        centroidO = newCentroid
        print(centroidO)


streetCode = [34510, 10030, 34050]
clos = closestCenter(streetCode, ())

map3 = dRDD.filter(lambda x: closestCenter(x, newCentroid)[0] == clos[0]).collect()
count = len(map3)
token = dict(cntr(map3))
cntr = len(token)
maxValue = max(token.items(), key=itemgetter(1))[1]
probability = round(count / (maxValue * cntr), 6)
print(probability)

spark.stop()
