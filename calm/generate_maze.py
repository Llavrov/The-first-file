#!/usr/bin/python
from collections import deque
import random
from matplotlib import patches
from matplotlib.collections import PatchCollection
import matplotlib.pyplot as plt
from itertools import chain
import argparse
import datetime


def get_neighbours(point, shape):
    i, j = point
    N, M = shape
    if i > 0:
        yield i - 1, j
    if j > 0:
        yield i, j - 1
    if i < N - 1:
        yield i + 1, j
    if j < M - 1:
        yield i, j + 1


def shuffle(x):
    l = list(x)
    random.shuffle(l)
    return l


def it_near(point, shape):
    return iter(shuffle(get_neighbours(point, shape)))


def find_solution(maze):
    shape, start, end = maze.shape, maze.start, maze.end

    state = deque()
    visited = set()
    state.append((start, it_near(start, shape)))
    visited.add(start)
    # generate solution
    while state:
        try:
            point = next(state[-1][1])
            #             debug and print(point)
            if not maze.can_go(state[-1][0], point):
                continue
            if point in visited:
                continue
            if point == end:
                return [s[0] for s in state] + [point]
            visited.add(point)
            state.append((point, it_near(point, shape)))
        except StopIteration:
            state.pop()
    raise ValueError("No Solution")


def dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


class Maze(object):
    def __init__(self, shape, start=None, end=None):
        self.start = tuple(start or (0, 0))
        self.end = tuple(end or (shape[0] - 1, shape[1] - 1))
        self.walls = set()
        self.shape = shape

    def add_wall(self, p1, p2):
        assert dist(p1, p2) == 1
        self.walls.add((p1, p2))
        self.walls.add((p2, p1))

    def can_go(self, p1, p2):
        return (p1, p2) not in self.walls

    def seed_walls(self, density=0.1, offset=3):
        N, M = self.shape
        for i in range(N):
            for j in range(M):
                wc = 1
                p1 = (i, j)
                if dist(p1, self.start) > offset and dist(p1, self.end) > offset:
                    nbrs = list(get_neighbours(p1, self.shape))
                    for p2 in nbrs:
                        if random.random() < density and wc < len(nbrs):
                            wc += 1
                            self.add_wall(p1, p2)

    @staticmethod
    def get_wall(p1, p2):
        s_i = (p1[0] + p2[0] + 1) // 2
        s_j = (p1[1] + p2[1] + 1) // 2
        e_i = (p1[0] + p2[0] + 2) // 2
        e_j = (p1[1] + p2[1] + 2) // 2
        return (s_i, e_i), (s_j, e_j), 'black'

    def draw(self, route=None, size=16, tight_lo=False, eqyaxi=False, save=False, filepath='./maze.png'):
        figsize = (size, self.shape[1] / self.shape[0] * size)
        plt.rcParams["figure.figsize"] = figsize
        plt.rcParams['lines.linewidth'] = 4
        fig, ax = plt.subplots()

        if eqyaxi:
            plt.axis('equal')
        if tight_lo:
            plt.tight_layout()
        plt.axis('off')
        plt.gca().invert_yaxis()
        N, M = self.shape
        plt.plot((0, N, N, 0, 0), (0, 0, M, M, 0), 'black')
        walls = []
        for p1, p2 in self.walls:
            if p1 < p2:
                walls.append(Maze.get_wall(p1, p2))
        plt.plot(*chain(*walls))

        if route is not None:
            plt.plot([p[0] + 0.5 for p in route], [p[1] + 0.5 for p in route], 'green')

        def shift(point, d):
            return point[0] + d, point[1] + d

        t = 0.2
        start = patches.Rectangle(shift(self.start, t / 2), 1 - t, 1 - t)
        finish = patches.Rectangle(shift(self.end, t / 2), 1 - t, 1 - t)
        collection = PatchCollection([start, finish])
        collection.set_color(['yellow', 'green'])
        ax.add_collection(collection)

        if save:
            plt.savefig(filepath)
        else:
            plt.show()


#     def get_neighbours(self, p):


def generate_maze(shape, start=None, end=None, debug=False, density=0.1, offset=3, retries=5, wallprob=0.5):
    attempts = 0
    solution = None
    maze = Maze(shape=shape, start=start, end=end)
    while attempts < retries:
        try:
            if density > 0:
                maze.seed_walls(density=density, offset=offset)
            solution = find_solution(maze)
            break
        except ValueError:
            attempts += 1
            maze = Maze(shape=shape, start=start, end=end)
    if solution is None:
        # maze.draw()
        raise Exception("Unable to find initial solution, try reducing seed density")

    # now go with dfs
    state = deque()
    path = deque()
    path.append(maze.start)
    state.append(it_near(maze.start, maze.shape))
    while state:
        try:
            curr = next(state[-1])
            prev = path[-1]
            debug and print(curr)
            if not maze.can_go(prev, curr):
                debug and print("Skipping - wall")
                continue
            if len(path) > 1 and curr == path[-2]:
                debug and print("Skipping - went back")
                continue
            if curr in path:  # looped
                if curr in solution and prev in solution and solution.index(curr) - solution.index(prev) in (-1, 1):  # not breaking solution
                    continue
                if wallprob == 1 or random.random() < wallprob:
                    maze.add_wall(prev, curr)
                    debug and print("Adding wall", prev, curr)
            else:
                state.append(it_near(curr, maze.shape))
                path.append(curr)
        except StopIteration:
            state.pop()
            path.pop()

    return maze, solution


def main(
        shape,
        start=None,
        end=None,
        random_endpoints=False,
        density=0.1,
        offset=3,
        retries=5,
        wallprob=0.5,
        save=False,
        maze_path='./maze.png',
        show_solution=False,
        solution_path='./solution.png',
        debug=False
):
    if not 0 <= density <= 1:
        raise ValueError("desity should be in [0,1]")
    if random_endpoints:
        N, M = shape
        start = (random.randint(0, N - 1), random.randint(0, M - 1))
        end = (random.randint(0, N - 1), random.randint(0, M - 1))
    maze, solution = generate_maze(
        shape=shape,
        start=start,
        end=end,
        wallprob=wallprob,
        density=density,
        offset=offset,
        retries=retries,
        debug=debug
    )

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    maze_path = maze_path or './maze_{}.png'.format(timestamp)
    solution_path = solution_path or './solution_{}.png'.format(timestamp)

    maze.draw(save=save, filepath=maze_path, tight_lo=True, eqyaxi=True)
    if show_solution:
        maze.draw(route=solution, save=save, filepath=solution_path, tight_lo=True, eqyaxi=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--shape', default=(25, 40), type=int, nargs='+')
    parser.add_argument('--start', default=None, type=int, nargs='+')
    parser.add_argument('--end',  default=None, type=int, nargs='+')
    parser.add_argument('--random-endpoints', '-r', action='store_true')
    parser.add_argument('--save', '-s', action='store_true')
    parser.add_argument('--maze-path', default=None)
    parser.add_argument('--show-solution', '--solution', action='store_true')
    parser.add_argument('--solution-path', default=None)
    parser.add_argument('--density', '-d', type=float, default=0, help='density of initial seed of walls - probability')
    parser.add_argument('--offset', '-o', type=int, default=3, help='offset from start and end for initial generation to reduce blocking probability')
    parser.add_argument('--wallprob', '-w', type=float, default=0.5, help='probabilty to place a wall upon encountering a loop')
    parser.add_argument('--debug', action='store_true')

    args = parser.parse_args()

    main(
        shape=args.shape,
        start=args.start,
        end=args.end,
        random_endpoints=args.random_endpoints,
        wallprob=args.wallprob,
        density=args.density,
        offset=args.offset,
        save=args.save,
        maze_path=args.maze_path,
        show_solution=args.show_solution,
        solution_path=args.solution_path,
        debug=args.debug
    )
