# ##
# roboagent - a robot pyamaze agent
# ##
from pyamaze import maze, agent, textLabel
from queue import PriorityQueue


def h(cell1, cell2):
    x1, y1 = cell1
    x2, y2 = cell2

    return abs(x1 - x2) + abs(y1 - y2)


def aStar(maze_inst):
    start = (maze_inst.rows, maze_inst.cols)
    g_score = {cell:float('inf') for cell in maze_inst.grid}
    g_score[start] = 0
    f_score = {cell:float('inf') for cell in maze_inst.grid}
    f_score[start] = h(start, (1, 1))

    pq = PriorityQueue()
    pq.put((h(start, (1, 1)), h(start, (1, 1)), start))
    aPath = {}
    while not pq.empty():
        currCell = pq.get()[2]
        if currCell == (1, 1):
            break
        for d in 'ESNW':
            if maze_inst.maze_map[currCell][d] == True:
                if d == 'E':
                    childCell = (currCell[0], currCell[1] + 1)
                if d == 'W':
                    childCell = (currCell[0], currCell[1] - 1)
                if d == 'N':
                    childCell = (currCell[0] - 1, currCell[1])
                if d == 'S':
                    childCell = (currCell[0] + 1, currCell[1])

                temp_g_score = g_score[currCell] + 1
                temp_f_score = temp_g_score + h(childCell, (1, 1))

                if temp_f_score < f_score[childCell]:
                    g_score[childCell] = temp_g_score
                    f_score[childCell] = temp_f_score
                    pq.put((temp_f_score, h(childCell, (1, 1)), childCell))
                    aPath[childCell] = currCell
    fwdPath = {}
    cell = (1, 1)
    while cell != start:
        fwdPath[aPath[cell]] = cell
        cell = aPath[cell]
    return fwdPath


if __name__ == '__main__':
    maze_inst = maze(5, 5)
    maze_inst.CreateMaze()
    path = aStar(maze_inst)

    a = agent(maze_inst, footprints=True)
    maze_inst.tracePath({a:path})
    l = textLabel(maze_inst, 'A Star Path Length', len(path) + 1)

    maze_inst.run()
