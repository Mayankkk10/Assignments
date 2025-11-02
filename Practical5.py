def LCS(s1, s2, m, n):
    c = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    b = [["" for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
                b[i][j] = "Diagonal"
            elif c[i - 1][j] >= c[i][j - 1]:
                c[i][j] = c[i - 1][j]
                b[i][j] = "Upward"
            else:
                c[i][j] = c[i][j - 1]
                b[i][j] = "Leftward"
    return c, b


def Print_LCS(b, s1, i, j):
    if i == 0 or j == 0:
        return
    if b[i][j] == "Diagonal":
        Print_LCS(b, s1, i - 1, j - 1)
        print(s1[i - 1], end="")
    elif b[i][j] == "Upward":
        Print_LCS(b, s1, i - 1, j)
    else:
        Print_LCS(b, s1, i, j - 1)


s1 = "AGCCTTAAGGCTACCTAGCTT"
s2 = "GACAGCCTACAAGGTTAGCTTG"
x = len(s1)
y = len(s2)
c, b = LCS(s1, s2, x, y)
Print_LCS(b, s1, x, y)
print("\n", c[x][y])


def LRS(s):
    n = len(s)
    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if s[i - 1] == s[j - 1] and i != j:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    i, j = n, n
    lrs = []
    while i > 0 and j > 0:
        if s[i - 1] == s[j - 1] and i != j:
            lrs.append(s[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    return ''.join(reversed(lrs))


s = "AABCBDC"
print("Longest Repeating Subsequence:", LRS(s))