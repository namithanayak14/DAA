"""
Usage: python3 plot.py --path [path to file]
Make sure to name the paths properly, (read code to understand how the file naming and folder nameing works)
"""

import argparse
import matplotlib.pyplot as pyplot
import os

parser = argparse.ArgumentParser(description="plot graphs for algorithm analysis")
parser.add_argument('--path', help="gives the path to file")
arguments = parser.parse_args()


path = arguments.path

f = open(path, "r")
size = []
value = []
for x in f:
  size.append(float(x.split()[0]))
  value.append(float(x.split()[1]))

ylabel = "Execution Time" if "Execution" in path else "Number of Comparisions"
title = path.split('/')[1]

directory = f'../images/{title}/'

try:
    os.mkdir('../images')
except:
    print("../images exists")

try:
    os.mkdir(directory)
except:
    print(f"{directory} exists")

pyplot.plot(size,value)
pyplot.xlabel('Size')
pyplot.ylabel(ylabel)
pyplot.title(title)
pyplot.savefig(f'../images/{title}/SizeVs{ylabel}.png')
