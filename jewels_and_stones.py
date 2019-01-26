J = "aA"
S = "aAAbbbb"


#------------------------


class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        J = set(J)
        S = list(S)
        Smap = dict()
        for s in S:
            if s in Smap:
                Smap[s] += 1
            else:
                Smap[s] = 1
        out = 0
        for j in J:
            out += Smap.get(j, 0)
        return out


if __name__ == '__main__':
    sol = Solution()
    res = sol.numJewelsInStones(J, S)
    print(res)
