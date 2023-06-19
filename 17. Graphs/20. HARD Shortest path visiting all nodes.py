# https://leetcode.com/problems/shortest-path-visiting-all-nodes/description/
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        # full explanation: https://leetcode.com/problems/shortest-path-visiting-all-nodes/solutions/178744/python-bfs-solution-with-optimization-beats-100/
        num_nodes = len(graph)
        
        masks = [1 << i for i in range(num_nodes)] # set bits indicates ith node is visited
        all_nodes_visited = (1<<num_nodes) - 1 # all nodes visited (11111...111)
        # state = node, state at which we visited this node
        queue = deque([(i, masks[i]) for i in range(num_nodes)])
        steps = 0

        visited_states = [set([masks[i]]) for i in range(num_nodes)] # ith index has ith mask indicated which state was visited with with this node, keep adding to this set for each node, visited added to queue

        while queue:
            level_size = len(queue)
            while level_size:
                node, visited = queue.popleft()
                if visited == all_nodes_visited:
                    return steps
                for neighbor in graph[node]:
                    new_visited = visited | masks[neighbor] # mark this node as visited
                    if new_visited == all_nodes_visited:
                        return steps + 1
                    if new_visited not in visited_states[neighbor]:
                        visited_states[neighbor].add(new_visited)
                        queue.append((neighbor, new_visited))
                level_size -= 1
            steps += 1
        return int(inf)