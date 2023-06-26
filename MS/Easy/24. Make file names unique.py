class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        seen = set()
        file_num_dict = collections.defaultdict(int)
        result = []
        for name in names:
            if name in seen:
                k = file_num_dict[name]
                new_name = name
                while new_name in seen:
                    k += 1
                    new_name = f'{name}({k})'
                file_num_dict[name] = k
                result.append(new_name)
                seen.add(new_name)
            else:
                result.append(name)
                seen.add(name)
                file_num_dict[name] = 0
        return result