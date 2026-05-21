class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        res_len = 0

        def expand(left, right):
            while (
                left >= 0 and
                right < len(s) and
                s[left] == s[right]
            ):
                left -= 1
                right += 1

            return s[left + 1:right]

        for i in range(len(s)):
            odd = expand(i, i)

            if len(odd) > res_len:
                res = odd
                res_len = len(odd)

            even = expand(i, i+1)

            if len(even) > res_len:
                res = even
                res_len = len(even)

        return res
