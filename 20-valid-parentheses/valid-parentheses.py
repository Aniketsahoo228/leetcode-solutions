class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for bracket in s:
            if bracket in "([{":
                stack.append(bracket)
            else:
                if not stack:
                    return False

                top = stack.pop()

                if bracket == ")" and top != "(":
                    return False
                if bracket == "]" and top != "[":
                    return False
                if bracket == "}" and top != "{":
                    return False

        return len(stack) == 0