# Matt Foutch Maze Project

from enum import Enum


class Status(Enum):
    UNVISITED = 0
    VISITED = 1


class Direction(Enum):
    STRAIGHT = 0
    DIAGONAL = 1


class Node:
    def __init__(self, x, y, jump):
        self.x = x
        self.y = y
        self.jump = jump
        self.status = Status.UNVISITED

    def __str__(self):
        if self.status == Status.UNVISITED:
            return "[" + str(self.y + 1) + "," + str(self.x + 1) + "] {" + str(self.jump) + "} U"
        else:
            return "[" + str(self.y + 1) + "," + str(self.x + 1) + "] {" + str(self.jump) + "} V"

    def visit(self):
        self.status = Status.VISITED


def loadfile():
    print("Opening testInput.txt")
    f = open("testInput", 'r')
    contents = f.readlines()                # Read in maze

    maze = []
    for i in range(1, len(contents)):

        maze.append(contents[i].split())     # save maze to array

    for i in range(0, len(maze)):
        print(maze[i])

    for i in range(0, len(maze)):          # change variable type to Node
        for j in range(0, len(maze[i])):
            maze[i][j] = Node(i, j, int(maze[i][j]))

    return maze


def solve(maze):
    path = []
    dfs(maze, maze[0][0], Direction.STRAIGHT)
    return path


def dfs(graph, node, direct):
    global solved
    if node.status == Status.UNVISITED:  # if we haven't been there before
        print(node)                      # tell us what node we're at
        node.visit()                     # change the node to visited

        if node.jump == 0:
            print(node)
            print("DONE")
            solved = True
            return

        if node.jump < 0:               # if landing on red, switch directions
            if direct == Direction.STRAIGHT:
                direct = Direction.DIAGONAL
            else:
                direct = Direction.STRAIGHT

        if direct == Direction.STRAIGHT:   # check all directions
            if 0 <= node.x + node.jump < 8:
                dfs(graph, graph[node.x + node.jump][node.y], direct)  # right
            if 0 <= node.x - node.jump < 8:
                dfs(graph, graph[node.x - node.jump][node.y], direct)  # left
            if 0 <= node.y + node.jump < 8:
                dfs(graph, graph[node.x][node.y + node.jump], direct)  # down
            if 0 <= node.y - node.jump < 8:
                dfs(graph, graph[node.x][node.y - node.jump], direct)  # up
        else:                           # check diagonal directions
            if 0 <= node.x + node.jump < 8:
                if 0 <= node.y + node.jump < 8:
                    dfs(graph, graph[node.x + node.jump][node.y + node.jump], direct)  # down right
                if 0 <= node.y - node.jump < 8:
                    dfs(graph, graph[node.x + node.jump][node.y - node.jump], direct)  # down left
            if 0 <= node.x - node.jump < 8:
                if 0 <= node.y + node.jump < 8:
                    dfs(graph, graph[node.x - node.jump][node.y + node.jump], direct)  # up right
                if 0 <= node.y - node.jump < 8:
                    dfs(graph, graph[node.x - node.jump][node.y - node.jump], direct)  # up left
        # print("Traceback")
        if solved:
            print(node)


def main():
    print("mazeProject")
    maze = loadfile()
    result = solve(maze)

    print(result)


solved = False
main()
