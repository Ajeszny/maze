import datetime
import sys

import matplotlib.pyplot as plt
import networkx as nx
import random

def draw_maze(graph, start, end, mst=False):
    # Rysowanie labiryntu
    plt.figure()
    plt.text(start[0], start[1]-0.5, "S")
    plt.text(end[0], end[1]-0.5, "E")
    for (u, v) in graph.edges():
        x1, y1 = u
        x2, y2 = v
        plt.plot([x1, x2], [y1, y2], linewidth=9, color='blue', zorder=1)
        plt.plot([x1, x2], [y1, y2], linewidth=5, color='white', zorder=2)
        if (mst):
            plt.plot([x1, x2], [y1, y2], linewidth=1, color='green', zorder = 3)

    plt.axis('off')
    plt.savefig('result.jpg')

def find_path(maze, start, end):
    path = nx.dijkstra_path(maze, start, end)
    return path

def draw_maze_with_path(maze, start, end, mst=False):
    path = find_path(maze, start, end)
    draw_maze(maze, start, end, mst=mst)
    for i in range(len(path) - 1):
        x1, y1 = path[i]
        x2, y2 = path[i + 1]
        plt.plot([x1, x2], [y1, y2], 'r-', linewidth=2)
    plt.savefig('maze2.png')

def generate_maze(m, n):
    graph = nx.grid_2d_graph(m, n)

    for (u, v) in graph.edges():
        graph.edges[u, v]['weight'] = random.randint(1, 3)

    mst = nx.minimum_spanning_tree(graph)

    finalgraph = nx.Graph()

    for (u, v) in mst.edges():
        finalgraph.add_edge(u, v)

    return finalgraph

def generate_pathmaze(m, n):
    graph = nx.grid_2d_graph(m, n)

    for (u, v) in graph.edges():
        graph.edges[u, v]['weight'] = 1

    snake_path = []
    for i in range(m):
        if i % 2 == 0:
            for j in range(n):
                snake_path.append((i, j))
        else:
            for j in range(n - 1, -1, -1):
                snake_path.append((i, j))

    for i in range(len(snake_path) - 1):
        u, v = snake_path[i], snake_path[i + 1]
        graph.edges[u, v]['weight'] = random.randint(4, 6)

    mst = nx.minimum_spanning_tree(graph)

    finalgraph = nx.Graph()

    for (u, v) in mst.edges():
        finalgraph.add_edge(u, v)

    return finalgraph


def task1(graph):
    mst = nx.minimum_spanning_tree(graph)
    print(mst)
    print(mst.nodes())


def task2(graph, start, end):
    draw_maze(graph, start, end)
    draw_maze_with_path(graph, start, end)

def task3(graph, start, end):
    draw_maze_with_path(graph, start, end, mst=True)

def task4(m, n, start, end):
    graph = generate_pathmaze(m, n)
    task2(graph, start, end)


if __name__ == "__main__":
    m = int(sys.argv[1])
    n = int(sys.argv[2])
    maze = generate_maze(m, n)
    task1(maze)
    t2 = datetime.datetime.now()
    task2(maze, (int(sys.argv[3]), int(sys.argv[4])), (int(sys.argv[5]), int(sys.argv[6])))
    t1 = datetime.datetime.now()
    print(f"{(t1-t2).microseconds//1000} ms elapsed")
