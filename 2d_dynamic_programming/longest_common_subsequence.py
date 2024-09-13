class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # First Row = text1, First Col = text2
        # dp = [[0]*row for i in range(col)]
        # Determining what to store in the rows and cols is cruciual
        dp = [[0]*len(text1) for i in range(len(text2))]

        # Populate row
        c,r = 0, 0
        while c < len(text1):
            if text1[c] == text2[0]:
                while (c < len(text1)):
                    dp[0][c] = 1
                    c = c + 1
            c = c + 1
        # Populate col
        while r < len(text2):
            if text2[r] == text1[0]:
                while (r < len(text2)):
                    dp[r][0] = 1
                    r = r + 1
            r = r + 1
            
        for r in range(1, len(text2)):
            for c in range(1, len(text1)):
                if text1[c] == text2[r]:
                    dp[r][c] = dp[r-1][c-1] + 1
                else:
                    dp[r][c] = max(dp[r-1][c], dp[r][c-1])

        print(dp)
        return dp[len(text2)-1][len(text1)-1]


        