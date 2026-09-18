class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = { a : [] for a in range(numCourses) }
        for src, dst in prerequisites:
            graph[dst].append(src)

        num_parents = { a : 0 for a in graph.keys() }
        for node in graph:
            for child in graph[node]:
                num_parents[child] += 1

        ready = [ node for node in graph if num_parents[node] == 0 ]
        order = []

        while ready:
            node = ready.pop()
            order.append(node)

            for child in graph[node]:
                num_parents[child] -= 1
                if num_parents[child] == 0:
                    ready.append(child)
        return len(order) == numCourses
