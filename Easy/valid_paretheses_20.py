class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        default = {
            '(':')',
            '[':']',
            '{':'}'
        }

        if len(s) <= 1:
            return False
        
        for k,v in enumerate(s,0):

            if v in default.keys():
                stack.append(v)
                continue

            if len(stack) and default.get(stack[-1], None) == v:
                stack.pop()
                continue
            else:
                return False

        if len(stack) == 0:
            return True
        
        return False

            

s = Solution()
print(s.isValid(")"))
