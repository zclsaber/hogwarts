class Solution:
    '''
    1. 执行用时：47ms， 击败 15.52%
    2. 消耗内存：16.34M， 击败 72.45%
    '''
    def longestCommonPrefix(self, strs) -> str:
        if len(strs) < 2:
            return strs[0]
        strs_len = [ len(s) for s in strs]
        shortest = min(strs_len)
        if shortest == 0:
            return ""
        common = ''
        for i in range(shortest):
            for s in strs:
                if s[i] != strs[0][i]:
                    flag = False
                    break
                else:
                    flag = True
            if flag:
                common += s[i]
            else:
                break
        if common == '':
            return ""
        else:
            return common

class SolutionLeetcodeOne:
    '''
    依次遍历字符串数组中的每个字符串，对于每个遍历到的字符串，更新最长公共前缀，当遍历完所有的字符串以后，即可得到字符串数组中的最长公共前缀。
    '''
    def longestCommonPrefix(self, strs) -> str:
        if not strs:
            return ""

        prefix, count = strs[0], len(strs)
        for i in range(1, count):
            prefix = self.lcp(prefix, strs[i])
            if not prefix:
                break

        return prefix

    def lcp(self, str1, str2):
        length, index = min(len(str1), len(str2)), 0
        while index < length and str1[index] == str2[index]:
            index += 1
        return str1[:index]

class SolutionLeetcodeTwo:
    '''
    纵向扫描时，从前往后遍历所有字符串的每一列，比较相同列上的字符是否相同，如果相同则继续对下一列进行比较，
    如果不相同则当前列不再属于公共前缀，当前列之前的部分为最长公共前缀。
    '''
    def longestCommonPrefix(self, strs) -> str:
        if not strs:
            return ""

        length, count = len(strs[0]), len(strs)
        for i in range(length):
            c = strs[0][i]
            if any(i == len(strs[j]) or strs[j][i] != c for j in range(1, count)):
                return strs[0][:i]

        return strs[0]


if __name__ == "__main__":
    strs = ["ab", "a"]
    print(Solution().longestCommonPrefix(strs))