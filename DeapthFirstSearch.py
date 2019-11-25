from collections import deque


def dfs(graph, start_node, end_node):
    frontier = deque()
    frontier.appendleft(start_node)
    explored = []
    while frontier:
        current_node = frontier.popleft()
        if current_node in explored:
            continue
        if current_node == end_node:
            return True

        for neighbor in graph[current_node]:
            frontier.appendleft(neighbor)
        explored.append(current_node)
