class Solution:
    
    ROMAN_NUMB = {
          'I':1, 
          'V':5,
          'X':10,
          'L':50,
          'C':100,
          'D':500,
          'M':1000
          }
    
    def romanToInt(self, s: str) -> int:
        res = 0

        if len(s) == 1:
            return self.ROMAN_NUMB.get(s)
        
        index = 0

        while index <= len(s)-1:
            a = self.ROMAN_NUMB.get(s[index],0)
            b = self.ROMAN_NUMB.get(s[index+1],0) if len(s)-1 >= index+1 else 0
            if a < b:
                res = res + (b - a)
                index +=1
            else:
                res += a
            index += 1
        return res

s = Solution()
print(s.romanToInt('MCMXCIV'))
print(s.romanToInt('III'))