class Solution:
    def isValid(self, s: str) -> bool:
        a = b = c = 0
        for i in s:
            if i == "(":
                a += 1
            if i == "{":
                b += 1
            if i == "[":
                c += 1
            if i == ")":
                a -= 1
            if i == "}":
                b -= 1
            if i == "]":
                c -= 1
        if a or b or c < 0:
            return False
        elif a or b or c > 0:
            return False

        else:
            return True

if __name__ == "__main__":
    s = "([)]"
    print(Solution().isValid(s))