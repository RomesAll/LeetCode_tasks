class Solution:
    #Поиск палиндрома
    def isPalindrome(self, x: int) -> bool:
        result = lambda x: True if x == x[::-1] else False
        return result(str(x))

s = Solution()
print(s.isPalindrome(121))