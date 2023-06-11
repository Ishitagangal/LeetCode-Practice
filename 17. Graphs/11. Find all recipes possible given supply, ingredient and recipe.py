class Node:
    def __init__(self):
        self.indegree = 0
        self.outnodes = []

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # make a graph of  ingredients  to recipes
        # zero degree nodes = supplies to start of
        graph = collections.defaultdict(Node)
        total_dependencies = 0

        for i, recipe in enumerate(recipes):
            for ingredient in ingredients[i]:
                graph[ingredient].outnodes.append(recipe)
                graph[recipe].indegree += 1
                total_dependencies += 1

        zero_degree_nodes = deque(supplies)
        recipes_set = set(recipes)
        result = []

        while zero_degree_nodes:
            supply = zero_degree_nodes.popleft()
            if supply not in graph:
                continue
            if supply in recipes_set:
                result.append(supply)
            for neighbor in graph[supply].outnodes:
                graph[neighbor].indegree -=1
                if graph[neighbor].indegree == 0:
                    zero_degree_nodes.append(neighbor)
        return result

