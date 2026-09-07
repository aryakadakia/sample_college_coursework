from collections import *


def bfs(start, goal):
    q = deque()
    q.append(start)
    back_dict = {}
    back_dict[start] = None

    while len(q) != 0:
        vertex = q.popleft()

        for v in vertex.adj_list:
            if not v in back_dict:
                back_dict[v] = vertex
                q.append(v)
                if v.name == goal.name:
                    end = v
                    path = [v]
                    while back_dict[end] is not None:
                        path.append(back_dict[end])
                        end = back_dict[end]
                    return path

    return []
