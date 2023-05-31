# Input: accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
# Output: [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
class Solution:
    def dfs(self, node, graph, visited, component):
        if visited[node]:
            return
        visited[node] = True
        component.append(node)
        for neighbor in graph[node]:
            if not visited[neighbor]:
                self.dfs(neighbor, graph, visited, component)
    
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = collections.defaultdict(set)
        visited = {}
        email_to_account = {}

        # set up graph, visited 
        for account in accounts:
            emails = account[1:]
            first_email = emails[0] # could've been last or any other
            for email in emails:
                # add undirected edges b/w first node and other nodes
                graph[email].add(first_email)
                graph[first_email].add(email)
                visited[email] = False
                email_to_account[email] = account[0] # name
        
        output = []
        for email,account in email_to_account.items():
            if visited[email]:
                continue
            # visited dict ensures that DFS gets called for every component
            # and NOT on every node
            nodes = [] # to fill all nodes (emails) in the component
            self.dfs(email, graph, visited, nodes)
            output.append([account] + sorted(nodes))
            
        return output