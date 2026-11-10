class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        result = []

        for val in strs:
            seen = {}
            for ch in val:
                seen[ch] = seen.get(ch, 0) + 1
            result.append(seen)

        prefix = ""

        for i in range(len(strs[0])):
            ch = strs[0][i]

            for j in range(len(strs)):
                # letter missing from the string's count dict, string too short, or wrong position
                if ch not in result[j] or i >= len(strs[j]) or strs[j][i] != ch:
                    return prefix

            prefix += ch

        return prefix