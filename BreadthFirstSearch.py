from collections import deque


def person_is_seller(name):
    return name[-1] == 'm'


def bfs(graph, name):
    search_que = deque()
    search_que += graph[name]
    searched = []
    while search_que:
        person = search_que.popleft()
        if person not in searched:
            if person_is_seller(person):
                print("%s is seller mango" % person)
            else:
                search_que += graph[person]
                searched.append(person)

    return False


graph = dict()
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph['claire'] = ["thom", "jonny"]
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []

bfs(graph, "you")
