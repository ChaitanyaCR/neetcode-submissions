class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        op = {}
        for str in strs:
                sorted_str = ''.join(sorted(str))
                if sorted_str in op:
                        op[sorted_str].append(str)
                else:
                        op[sorted_str] = [str]
        return list(op.values())
