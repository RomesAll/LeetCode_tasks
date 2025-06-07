class Solution:
    def longestCommonPrefix(self, strs) -> str:
        res_string = ''
        first_element_strs = strs[0] if len(strs) > 1 else None
        count_pref = 0

        if not first_element_strs:
            return "" if len(strs) == 0 else strs[0]

        for char in first_element_strs:
            for element_strs in strs:
                if res_string + char == element_strs[:len(res_string)+1]:
                    count_pref += 1

            if count_pref == len(strs):
                res_string += char
            
            count_pref = 0

        return res_string

s = Solution()
print(s.longestCommonPrefix(["reflower","flow","flight"]))