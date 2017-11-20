ans, start, end = 0, 0, 0
countDict = {}
s = "abcabcbb"
for c in s:
    end += 1
    countDict[c] = countDict.get(c, 0) + 1
    while countDict[c] > 1:
        countDict[s[start]] -= 1
        start += 1
        ans = max(ans, end - start)
print ans