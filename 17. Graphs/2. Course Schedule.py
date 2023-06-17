class Node:
    def __init__(self):
        self.indegrees = 0
        self.outNodes = []

class Solution:
    def canFinish(self, numCourses:int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(Node)
        totalDependencies = 0
        for prereq in prerequisites:
            nextCourse, prevCourse = prereq[0], prereq[1]
            graph[prevCourse].outNodes.append(nextCourse)
            graph[nextCourse].indegrees += 1
            totalDependencies += 1
        
        zeroDegreeCourses = []
        for index, node in graph.items():
            if node.indegrees ==0:
                zeroDegreeCourses.append(index)
        
        removedEdges = 0
        while zeroDegreeCourses:
            course = zeroDegreeCourses.pop()
            
            for nextCourse in graph[course].outNodes:
                graph[nextCourse].indegrees -=1
                removedEdges +=1
                if graph[nextCourse].indegrees ==0:
                    zeroDegreeCourses.append(nextCourse)
                    
        if removedEdges == totalDependencies:
            return True
        return False
            
    ## Detect cycle with DFS
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        for prereq in prerequisites:
            nextCourse, prevCourse = prereq[0], prereq[1]
            graph[prevCourse].append(nextCourse)
        
        visited = [False]* numCourses
        for current in range(numCourses):
            if self.isCyclic(current, graph, visited):
                return False
        return True
    
    def isCyclic(self, currentCourse, graph, visited):
        if visited[currentCourse]:
            return True # cycle detected
        
        visited[currentCourse] = True
        flag = False
        for child in graph[currentCourse]:
            flag = self.isCyclic(child, graph, visited)
            if flag:
                break # cycle detected
        visited[currentCourse] = False
        return flag
