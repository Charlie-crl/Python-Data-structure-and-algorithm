class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        dight_str = ''.join(list(map(str, digits)))
        answer = str(eval(dight_str+"+1"))
        return list(map(int,list(answer)))