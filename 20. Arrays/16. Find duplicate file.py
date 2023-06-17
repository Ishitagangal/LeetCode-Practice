class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_to_file = collections.defaultdict(list)
        for path in paths:
            components = path.split()
            root = components[0]
            for file in components[1:]:
                name, _, content = file.partition("(")
                content_to_file[content[:-1]].append(root +"/" + name)
        
        return [x for x in content_to_file.values() if len(x) > 1]