class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # 将p转为数字与字母结合的列表模式
        lstp = []
        lstch = []
        for index, ch in enumerate(p):
            if ch.isalpha() and lstp == []:
                lstp.append([0, 0])
                lstp.append(ch)
                lstch.append(ch)
            elif ch.isalpha() and index == len(p) - 1:
                lstp.append(ch)
                lstp.append([0, 0])
                lstch.append(ch)
            elif ch.isalpha():
                lstp.append(ch)
                lstch.append(ch)
            else:
                if ch == '*' and (lstp == [] or type(lstp[len(lstp)-1]) == str):
                    lstp.append([0, 100])
                elif ch == '.' and (lstp == [] or type(lstp[len(lstp)-1]) == str):
                    lstp.append([1, 1])
                elif type(lstp[len(lstp)-1]) == list and ch == '.':
                    newList = self.sumList(lstp[len(lstp)-1], [1, 1])
                    lstp[len(lstp)-1] = newList
                elif type(lstp[len(lstp)-1]) == list and ch == '*':
                    newList = self.sumList(lstp[len(lstp)-1], [0, 100])
                    lstp[len(lstp)-1] = newList

        lstch.append('$')

        # print(lstp)
        # print(lstch)
        # 开始转换s
        lsts = []
        targetch = 0
        for index, ch in enumerate(s):
            try:
                if ch != lstch[targetch] and (lsts == [] or type(lsts[len(lsts)-1]) == str):
                    lsts.append(1)
                elif ch != lstch[targetch] and type(lsts[len(lsts)-1]) == int:
                    lsts[len(lsts)-1] += 1
                elif ch == lstch[targetch] and index == len(s) - 1:
                    lsts.append(ch)
                    lsts.append(0)
                elif ch == lstch[targetch] and (lsts == [] or type(lsts[len(lsts)-1]) == str):
                    lsts.append(0)
                    lsts.append(ch)
                    targetch += 1
                elif ch == lstch[targetch]:
                    lsts.append(ch)
                    targetch += 1
            except IndexError:
                return False

        # print(lsts)
        # 开始匹配lsts和lstp
        if len(lsts) != len(lstp):
            return False

        ret = True
        for i in range(len(lsts)):
            if type(lsts[i]) == int and type(lstp[i]) == list:
                if lstp[i][0] <= lsts[i] <= lstp[i][1]:
                    pass
                else:
                    ret = False
            elif type(lsts[i]) == str and type(lstp[i]) == str:
                if lsts[i] == lstp[i]:
                    pass
                else:
                    ret = False
            else:
                ret = False

        return ret

    def sumList(self, lst01, lst02):
        lst = [lst01[0]+lst02[0], lst01[1]+lst02[1]]
        return lst


x = Solution()
print(x.isMatch(s='aa', p='a*'))

