"""
You are given a license key represented as a string s that consists of only alphanumeric characters and dashes. The string is separated into n + 1 groups by n dashes. You are also given an integer k.

We want to reformat the string s such that each group contains exactly k characters, except for the first group, which could be shorter than k but still must contain at least one character. Furthermore, there must be a dash inserted between two groups, and you should convert all lowercase letters to uppercase.

Return the reformatted license key.

 

Example 1:

Input: s = "5F3Z-2e-9-w", k = 4
Output: "5F3Z-2E9W"
Explanation: The string s has been split into two parts, each part has 4 characters.
Note that the two extra dashes are not needed and can be removed.
Example 2:

Input: s = "2-5g-3-J", k = 2
Output: "2-5G-3J"
Explanation: The string s has been split into three parts, each part has 2 characters except the first part as it could be shorter as mentioned above.
 

Constraints:

1 <= s.length <= 105
s consists of English letters, digits, and dashes '-'.
1 <= k <= 104
"""

# MY SOLUTION - using lists
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = [i.upper() for i in s.replace("-","")]
        res = []
        if len(s) % k == 0:
            while True:
                for _ in range(k):
                    res.append(s.pop(0))
                if len(s) == 0:
                    break
                res.append("-")
        else:
            for _ in range(len(s) % k):
                res.append(s.pop(0))
            res.append("-")
            while True:
                for _ in range(k):
                    res.append(s.pop(0))
                if len(s) == 0:
                    break
                res.append("-")
        return "".join(res)
    

# To test
# from LicenseKeyFormatting import Solution
# sol = Solution()
# sol.licenseKeyFormatting("2-5g-3-J", 2)



# INTERNET SOLUTION
# class Solution:
#     def licenseKeyFormatting(self, s: str, k: int) -> str:
#         temp = ""
#         n = len(s)
#         for i in range(0,n):
#             if(s[i] != '-'):
#                 temp += s[i].upper()
#         length = len(temp)
#         ans = ""
#         val = k
#         for i in range(length - 1,-1,-1):
#             if(val == 0):
#                 val = k
#                 ans += '-'
#             ans += temp[i]
#             val -= 1
#         ans = ans[::-1]
#         return ans