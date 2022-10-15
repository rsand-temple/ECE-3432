###
# obs2maze - converts robot observations into pyamaze data
#
# Input format:
#   '(3, 2)',0.22,1.2,0.14,1.8
#   '(4, 2)',1.1,1.2,1.3,0.12
#
# Output format:
#   (1, 1): {'E': 1, 'W': 0, 'N': 0, 'S': 0}
#   (2, 1): {'E': 0, 'W': 0, 'N': 0, 'S': 1}
#   (3, 1): {'E': 0, 'W': 0, 'N': 1, 'S': 1}
###
import csv

# open sampled maze
with open('./data/sample.maze', 'r') as f:
    for l in csv.reader(f, quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL, skipinitialspace=True):
        # parse each line
        north = float(l[1])
        south = float(l[2])
        east = float(l[3])
        west = float(l[4])
        coords = l[0]
        coords = coords[coords.index("(") + 1:coords.rindex(")")]
        c = coords.split(",")
        x = int(c[0])
        y = int(c[1])
        print(x, ",", y, ":", north, south, east, west)