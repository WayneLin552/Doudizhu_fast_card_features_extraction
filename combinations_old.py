############################################################################################
#  BLACK-JOKER RED-JOKER TWO THREE FOUR FIVE SIX SEVEN EIGHT NINE TEN JACK QUEEN KING ACE  #
############################################################################################
# import numpy as np

def toCards(*args):
    res = [0] * 15
    total = 0
    for idx, num in args:
        res[idx] += num
        total += num
    return total, tuple(res)
#toCards((a1,b1),(a2,b2))面值为牌a1的有b1张，a2有b2张，总共b1+b2张


rg = range(2, 15) #除去大小王（大王=1，小王=0），2-15为2-10,J,Q,K,A

# ROCKET~!
def getRocket():
    return [toCards((0, 1), (1, 1))]
# Pair/Tri/Quad
def getGroup():
    res = []
    for i in (4, 3, 2):
        for j in rg:
            res.append(toCards((j, i)))
    return res
# Tri&Lone/Tri&Pair/Quad&Pair 444422 444412 and so on
def getTeam():
    res = []
    for x, y in ((3, 1), (3, 2), (4, 2)):
        for i in rg:
            for j in rg:
                if j != i:
                    res.append(toCards((i, x), (j, y)))
    x=4
    y=1
    z=1
    for i in rg:
        for j in rg:
            for k in rg:
                if j!=i & j!=k & i!=k:
                    res.append(toCards((i,x),(j,y),(k,z)))
    
    x=4
    y=2
    z=2
    for i in rg:
        for j in rg:
            for k in rg:
                if j!=i & j!=k & i!=k:
                    res.append(toCards((i,x),(j,y),(k,z)))
                        
    return res
# Single/Double/Triple Sequence
def getSeq():
    res = []
    for weight, head, tail in ((1, 5, 13), (2, 3, 11), (3, 2, 7)):
        for length in range(head, tail):
            for s in range(3, 16 - length):
                res.append(toCards(*((x, weight) for x in range(s, s + length))))
    return res

def enumC(N, M): #N中选M张的可能组合
    def core(h, m):
        return tuple(
            (x, *ys)
                for x in range(h, N + 1 - m)
                    for ys in core(x + 1, m - 1)
        ) if m > 0 else ((),)
    return core(0, M)
C_08_2 = enumC(8, 2)
C_09_2 = enumC(9, 2)
C_09_4 = enumC(9, 4)
C_10_3 = enumC(10, 3)
C_11_2 = enumC(11, 2)
C_12_2 = enumC(12, 2)
C_12_3 = enumC(12, 3)
C_13_2 = enumC(13, 2)
C_13_3 = enumC(13, 3)
C_13_4 = enumC(13, 4)
C_13_5 = enumC(13, 5)

def extractFrame(s, l): #在牌0-15表示的列表中去除s~s+l(L)号以及大小王后的牌2-s-1~s+l-15
    return (
        tuple((x, 3) for x in range(s, s + l)),
        list(range(2, s)) + list(range(s + l, 15))
    )

# Alpha Plane  飞机+单数牌 如333444+56
def getPlaneAlpha():
    res = []
    # Length: 2 例如333444+56 333444+55
    for s in range(3, 14):
        tf, la = extractFrame(s, 2) #tf选中的作为飞机牌(a,3张)，la是剩下的
        ### C(13, 2) 去掉大小王，剩下13类牌，选两张做单牌 共0-15 15类牌
        for t in C_13_2: #从13类牌中各选一张作为带子
            tw = tuple((rg[i], 1) for i in t)
            res.append(toCards(*tf, *tw))
        ### C(11, 1) 去掉大小王以及飞机牌，剩下11类牌，从中选一类作为对子凑合
        for i in range(0, 11):
            wi = (la[i], 2)
            res.append(toCards(*tf, wi))
    # Length: 3 
    for s in range(3, 13):
        tf, la = extractFrame(s, 3)
        ### C(13, 3) 去掉大小王，剩下13类牌，选3张做单牌 共0-15 15类牌
        for t in C_13_3:
            tw = tuple((rg[i], 1) for i in t)
            res.append(toCards(*tf, *tw))
        ### 例如 333444555+678 333444555+667
        ### C(10, 1) * C(12, 1) 去大小王，飞机牌剩10类 选1做对子+去大小王和选的对子剩12类，选1做非对子
        for x in la:
            wx = (x, 2)
            for y in rg:
                if y != x:
                    wy = (y, 1)
                    res.append(toCards(*tf, wx, wy))
    # Length: 4 如333444555666+789J +7789 +7788 +7777
    for s in range(3, 12):
        tf, la = extractFrame(s, 4)
        ### C(13, 4)
        for t in C_13_4:
            tw = ((rg[i], 1) for i in t)
            res.append(toCards(*tf, *tw))
        ### C(9, 2)
        for t in C_09_2:
            tw = ((la[i], 2) for i in t)
            res.append(toCards(*tf, *tw))
        ### C(9, 1)
        for x in la:
            wx = (x, 4)
            res.append(toCards(*tf, wx))
        ### C(9, 1) * C(12, 2)
        for x in la:
            wx = (x, 2)
            ta = tuple(y for y in rg if y != x)
            for t in C_12_2:
                twy = tuple((ta[j], 1) for j in t)
                res.append(toCards(*tf, wx, *twy))
        ### C(9, 1) * C(12, 1)
        for x in la:
            wx = (x, 3)
            for y in rg:
                if y != x:
                    wy = (y, 1)
                    res.append(toCards(*tf, wx, wy))
    # Length: 5 333444555666777+ 因为最多17张or20张牌(地主)
    for s in range(3, 11):
        tf, la = extractFrame(s, 5)
        ### C(13, 5) 5单
        for t in C_13_5:
            tw = ((rg[i], 1) for i in t)
            res.append(toCards(*tf, *tw))
        ### C(8, 1) * C(12, 3) 1对子3单
        for x in la:
            wx = (x, 2)
            ta = tuple(y for y in rg if y != x)
            for t in C_12_3:
                twy = tuple((ta[j], 1) for j in t)
                res.append(toCards(*tf, wx, *twy))
        ### C(8, 2) * C(11, 1) 2对子1单
        for t in C_08_2:
            twx = tuple((la[i], 2) for i in t)
            ta = tuple(y for y in rg if y != la[t[0]] and y != la[t[1]])
            for y in ta:
                wy = (y, 1)
                res.append(toCards(*tf, *twx, wy))
        ### C(8, 1) * C(12, 2) 1个3，2个单
        for x in la:
            wx = (x, 3)
            ta = tuple(y for y in rg if y != x)
            for t in C_12_2:
                twy = tuple((ta[j], 1) for j in t)
                res.append(toCards(*tf, wx, *twy))
        ### C(8, 1) * C(7, 1) 一个3一个对子
        for x in la:
            wx = (x, 3)
            for y in la:
                if y != x:
                    wy = (y, 2)
                    res.append(toCards(*tf, wx, wy))
        ### C(8, 1) * C(12, 1) 一个炸弹一个对子
        for x in la:
            wx = (x, 4)
            for y in rg:
                if y != x:
                    wy = (y, 1)
                    res.append(toCards(*tf, wx, wy))
    return res

# Beta Plane 飞机+对子 如333444+5566
def getPlaneBeta():
    res = []
    # Length: 2
    for s in range(3, 14):
        tf, la = extractFrame(s, 2)
        ### C(11, 2) 去掉大小王和飞机类 剩下15-4=11类 选2类对子
        for t in C_11_2:
            tw = tuple((la[i], 2) for i in t)
            res.append(toCards(*tf, *tw))
        ### C(11, 1) 选4张直接炸弹做对子
        for x in la:
            wx = (x, 4)
            res.append(toCards(*tf, wx))
    # Length: 3
    for s in range(3, 13):
        tf, la = extractFrame(s, 3)
        ### C(10, 3) 剩10类选3类做对子  注意牌一共只有17张or20张（地主）
        for t in C_10_3:
            tw = tuple((la[i], 2) for i in t)
            res.append(toCards(*tf, *tw))
        ### C(10, 1) * C(9, 1) 一个对子一个炸弹
        for x in la:
            wx = (x, 4)
            for y in la:
                if y != x:
                    wy = (y, 2)
                    res.append(toCards(*tf, wx, wy))
    # Length: 4
    for s in range(3, 12):
        tf, la = extractFrame(s, 4)
        ### C(9, 4) 选4类做对子 共12+8=20 只有地主做得到 春天
        for t in C_09_4:
            tw = tuple((la[i], 2) for i in t)
            res.append(toCards(*tf, *tw))
        ### C(9, 2) 选2类炸弹 333444555666+7777+8888
        for t in C_09_2:
            tw = tuple((la[i], 4) for i in t)
            res.append(toCards(*tf, *tw))
        ### C(9, 1) * C(8, 2) 一个炸弹2个对子
        for x in la:
            wx = (x, 4)
            ta = tuple(y for y in la if y != x)
            for t in C_08_2:
                twy = tuple((ta[j], 2) for j in t)
                res.append(toCards(*tf, wx, *twy))
    return res

def getAllCombinations(): #set(l)去除重复项，sorted升序排列，c[1]取牌矩阵
    l = []
    funcs = (getRocket, getGroup, getTeam, getSeq, getPlaneAlpha, getPlaneBeta)
    for f in funcs:
        l += f()
    return tuple(c[1] for c in sorted(set(l)))

# static
allCombinations = getAllCombinations()
# arrayallCombinations = np.array(getAllCombinations())