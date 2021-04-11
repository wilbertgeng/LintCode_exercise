"""426 · Restore IP Addresses"""
class Solution:
    """
    @param s: the IP string
    @return: All possible valid IP addresses
    """
    def restoreIpAddresses(self, s):
        # write your code here
        res = []
        self.dfs(s, 0, "", res)
        return res

    def dfs(self, s, cnt, path, res):
        if cnt == 3 and len(s) > 3:
            return
        if cnt == 4 and len(s) > 0:
            return
        if cnt == 4 and len(s) == 0:
            res.append(path[:-1])
            return

        for i in range(1, 4):
            if i > len(s):
                break
            if int(s[:i]) > 255 or (i > 1 and s[0] == "0"):
                continue
            self.dfs(s[i:], cnt + 1, path + s[:i] + ".", res)
