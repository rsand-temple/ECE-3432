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
import numpy as np

THRESHOLD = 0.25
maze_py = []

# open sampled maze
with open('./data/sample.obs', 'r') as f:
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
        maze_py.append([x, y, north, south, east, west])

maze = np.zeros((len(maze_py), 6))

for i in range(len(maze_py)):
    maze[i][0] = maze_py[i][0]
    maze[i][1] = maze_py[i][1]
    maze[i][2] = (maze_py[i][2] < THRESHOLD)
    maze[i][3] = (maze_py[i][3] < THRESHOLD)
    maze[i][4] = (maze_py[i][4] < THRESHOLD)
    maze[i][5] = (maze_py[i][5] < THRESHOLD)
    
maze = maze[np.lexsort((maze[:,1],maze[:,0]))].astype(int)

with open('./data/sample.maze', 'w') as f:
    for i in range(len(maze_py)):
        nextline = "({},{}): {{ \'E\': {}, \'W\': {}, \'N\': {}, \'S\': {} }}".format(maze[i][0], maze[i][1], maze[i][2], maze[i][3], maze[i][4], maze[i][5])
        print(nextline)
        f.write(nextline)
        f.write('\n')
