############################################################################################
#  BLACK-JOKER RED-JOKER TWO THREE FOUR FIVE SIX SEVEN EIGHT NINE TEN JACK QUEEN KING ACE  #
############################################################################################

import numpy as np

# Tuple Form
def _T_cardsFrom(*args):
    res = [0] * 15
    for idx, num in args:
        res[idx] += num
    return tuple(res)
def _T_cardsCount(c):
    return sum(c)
def _T_cardsGrEq(cA, cB):
    for a, b in zip(cA, cB):
        if a < b:
            return False
    return True
def _T_cardsSubtract(cA, cB):
    return tuple(a - b for a, b in zip(cA, cB))


# Bit Form
# BITS = (0, 1, 3, 7, 15)
# #0张：0 1张：1 2张：1 1=3 3张：1 1 1=7 4张：1 1 1 1=15
# def _B_cardsFrom(*args):
#     tmp = [0] * 15
#     for idx, num in args:
#         tmp[idx] += num
#     res = 0
#     for num in tmp:
#         res |= BITS[num] #将新的四位表示好 0000==>XXXX
#         res <<= 4 #左移四位，为下一张牌腾出空间XXXX ==> XXXX0000
#     # print(res)
#     return res

def _B_cardsFrom(*args):
    tmp = [0] * 15
    dic = ['0000','0001','0011','0111','1111']
    for idx, num in args:
        tmp[idx] += num
    res = ''
    for num in tmp:
        res += dic[num] #将新的四位表示好 0000==>XXXX
    # print(res)
    return int(res+'0000',2)

# import time
# lmw1=[]
# old1=[]


# handA=(0, 1), (1, 1), (2, 3), (5, 2), (6, 3), (7, 2), (8, 1), (9, 1), (11, 1), (13, 1), (14, 1)
# time1 = time.time()
# for i in range(100000):
#     num = _B_cardsFrom((2, 1), (4, 2), (5, 1), (6, 1), (7, 1), (8, 2), (10, 1), (11, 4), (12, 1), (13, 3))
#     old1.append(num)
# time1end = time.time()-time1

# time2 = time.time()
# for i in range(100000):
#     num = _B_cardsFromlmw((2, 1), (4, 2), (5, 1), (6, 1), (7, 1), (8, 2), (10, 1), (11, 4), (12, 1), (13, 3))
#     lmw1.append(num)
# time2end = time.time()-time2

# print(time1end,time2end)

# def _B_cardsCount(c):
#     res = 0
#     #idx = 0
#     while c > 0:
#         res += 1
#         c &= c - 1 #比如001101110001少一张& 001101110000再少一张-1==>001101101111-1=001101101110 &==>001101100000
#     return res

def _B_cardsCount(c):
    return bin(c)[2:].count('1')

# def _B_cardsIdentity(c):
#     txt = bin(c)[2:]
#     length = len(txt)
#     idx = 0
#     while length > (length % 4):
#         if '1' in txt[length-4:length]:
#             idx += 1
#         length -= 4
#     if '1' in txt[:length]:
#         idx +=1
#     return idx
    




def _B_cardsGrEq(cA, cB):
    return cA & cB == cB #例如A11111111 B00110001 A&B00110001 说明A中有B
MASKS = (
    0x1111111111111110,
    0x2222222222222220,
    0x4444444444444440,
    0x8888888888888880,
)
def _B_cardsSubtract(cA, cB):
    tmp = cA ^ cB
    c1, c2, c3, c4 = tuple((tmp & MASKS[i]) >> i for i in (0, 1, 2, 3))
    # settle: 1st round
    c2, c1 = c2 & c1, c2 | c1
    c3, c2 = c3 & c2, c3 | c2
    c4, c3 = c4 & c3, c4 | c3
    # settle: 2nd round
    c2, c1 = c2 & c1, c2 | c1
    c3, c2 = c3 & c2, c3 | c2
    # settle: 3rd round
    c2, c1 = c2 & c1, c2 | c1
    return c1 | (c2 << 1) | (c3 << 2) | (c4 << 3)




#cardsFrom, cardsCount, cardsGrEq, cardsSubtract = _T_cardsFrom, _T_cardsCount, _T_cardsGrEq, _T_cardsSubtract
cardsFrom_old, cardsFrom, cardsCount, cardsGrEq, cardsSubtract =_T_cardsFrom, _B_cardsFrom, _B_cardsCount, _B_cardsGrEq, _B_cardsSubtract



# constant
rg = range(2, 15)

# ROCKET~!
def getRocket():
    return [cardsFrom((0, 1), (1, 1))]
# Pair/Tri/Quad
def getGroup():
    res = []
    for i in (4, 3, 2):
        for j in rg:
            res.append(cardsFrom((j, i)))
    return res
# Tri&Lone/Tri&Pair/Quad&Pair
def getTeam():
    res = []
    for x, y in ((3, 1), (3, 2), (4, 2)):
        for i in rg:
            for j in rg:
                if j != i:
                    res.append(cardsFrom((i, x), (j, y)))
    x=4
    y=1
    z=1
    for i in rg:
        for j in rg:
            for k in rg:
                if j!=i & j!=k & i!=k:
                    res.append(cardsFrom((i,x),(j,y),(k,z)))
    
    x=4
    y=2
    z=2
    for i in rg:
        for j in rg:
            for k in rg:
                if j!=i & j!=k & i!=k:
                    res.append(cardsFrom((i,x),(j,y),(k,z)))
    return res
# Single/Double/Triple Sequence
def getSeq():
    res = []
    for weight, head, tail in ((1, 5, 13), (2, 3, 11), (3, 2, 7)):
        for length in range(head, tail):
            for s in range(3, 16 - length):
                res.append(cardsFrom(*((x, weight) for x in range(s, s + length))))
    return res

def enumC(N, M):
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

def extractFrame(s, l):
    return (
        tuple((x, 3) for x in range(s, s + l)),
        list(range(2, s)) + list(range(s + l, 15))
    )

# Alpha Plane
def getPlaneAlpha():
    res = []
    # Length: 2
    for s in range(3, 14):
        tf, la = extractFrame(s, 2)
        ### C(13, 2)
        for t in C_13_2:
            tw = tuple((rg[i], 1) for i in t)
            res.append(cardsFrom(*tf, *tw))
        ### C(11, 1)
        for i in range(0, 11):
            wi = (la[i], 2)
            res.append(cardsFrom(*tf, wi))
    # Length: 3
    for s in range(3, 13):
        tf, la = extractFrame(s, 3)
        ### C(13, 3)
        for t in C_13_3:
            tw = tuple((rg[i], 1) for i in t)
            res.append(cardsFrom(*tf, *tw))
        ### C(10, 1) * C(12, 1)
        for x in la:
            wx = (x, 2)
            for y in rg:
                if y != x:
                    wy = (y, 1)
                    res.append(cardsFrom(*tf, wx, wy))
    # Length: 4
    for s in range(3, 12):
        tf, la = extractFrame(s, 4)
        ### C(13, 4)
        for t in C_13_4:
            tw = ((rg[i], 1) for i in t)
            res.append(cardsFrom(*tf, *tw))
        ### C(9, 2)
        for t in C_09_2:
            tw = ((la[i], 2) for i in t)
            res.append(cardsFrom(*tf, *tw))
        ### C(9, 1)
        for x in la:
            wx = (x, 4)
            res.append(cardsFrom(*tf, wx))
        ### C(9, 1) * C(12, 2)
        for x in la:
            wx = (x, 2)
            ta = tuple(y for y in rg if y != x)
            for t in C_12_2:
                twy = tuple((ta[j], 1) for j in t)
                res.append(cardsFrom(*tf, wx, *twy))
        ### C(9, 1) * C(12, 1)
        for x in la:
            wx = (x, 3)
            for y in rg:
                if y != x:
                    wy = (y, 1)
                    res.append(cardsFrom(*tf, wx, wy))
    # Length: 5
    for s in range(3, 11):
        tf, la = extractFrame(s, 5)
        ### C(13, 5)
        for t in C_13_5:
            tw = ((rg[i], 1) for i in t)
            res.append(cardsFrom(*tf, *tw))
        ### C(8, 1) * C(12, 3)
        for x in la:
            wx = (x, 2)
            ta = tuple(y for y in rg if y != x)
            for t in C_12_3:
                twy = tuple((ta[j], 1) for j in t)
                res.append(cardsFrom(*tf, wx, *twy))
        ### C(8, 2) * C(11, 1)
        for t in C_08_2:
            twx = tuple((la[i], 2) for i in t)
            ta = tuple(y for y in rg if y != la[t[0]] and y != la[t[1]])
            for y in ta:
                wy = (y, 1)
                res.append(cardsFrom(*tf, *twx, wy))
        ### C(8, 1) * C(12, 2)
        for x in la:
            wx = (x, 3)
            ta = tuple(y for y in rg if y != x)
            for t in C_12_2:
                twy = tuple((ta[j], 1) for j in t)
                res.append(cardsFrom(*tf, wx, *twy))
        ### C(8, 1) * C(7, 1)
        for x in la:
            wx = (x, 3)
            for y in la:
                if y != x:
                    wy = (y, 2)
                    res.append(cardsFrom(*tf, wx, wy))
        ### C(8, 1) * C(12, 1)
        for x in la:
            wx = (x, 4)
            for y in rg:
                if y != x:
                    wy = (y, 1)
                    res.append(cardsFrom(*tf, wx, wy))
    return res

# Beta Plane
def getPlaneBeta():
    res = []
    # Length: 2
    for s in range(3, 14):
        tf, la = extractFrame(s, 2)
        ### C(11, 2)
        for t in C_11_2:
            tw = tuple((la[i], 2) for i in t)
            res.append(cardsFrom(*tf, *tw))
        ### C(11, 1)
        for x in la:
            wx = (x, 4)
            res.append(cardsFrom(*tf, wx))
    # Length: 3
    for s in range(3, 13):
        tf, la = extractFrame(s, 3)
        ### C(10, 3)
        for t in C_10_3:
            tw = tuple((la[i], 2) for i in t)
            res.append(cardsFrom(*tf, *tw))
        ### C(10, 1) * C(9, 1)
        for x in la:
            wx = (x, 4)
            for y in la:
                if y != x:
                    wy = (y, 2)
                    res.append(cardsFrom(*tf, wx, wy))
    # Length: 4
    for s in range(3, 12):
        tf, la = extractFrame(s, 4)
        ### C(9, 4)
        for t in C_09_4:
            tw = tuple((la[i], 2) for i in t)
            res.append(cardsFrom(*tf, *tw))
        ### C(9, 2)
        for t in C_09_2:
            tw = tuple((la[i], 4) for i in t)
            res.append(cardsFrom(*tf, *tw))
        ### C(9, 1) * C(8, 2)
        for x in la:
            wx = (x, 4)
            ta = tuple(y for y in la if y != x)
            for t in C_08_2:
                twy = tuple((ta[j], 2) for j in t)
                res.append(cardsFrom(*tf, wx, *twy))
    return res

def getAllCombinations():
    l = []
    funcs = (getRocket, getGroup, getTeam, getSeq, getPlaneAlpha, getPlaneBeta)
    for f in funcs:
        l += f()
    # remove dulplicates
    # add count-info for sorting
    l = tuple((cardsCount(c), c) for c in set(l))
    # strip count-info
    return tuple(c for _, c in sorted(l))

# def lowerBound(combinations):
#     length = len(combinations)
#     if length <= 1:
#         return 0
#     flag = -1
#     idx = cardsIdentity[flag]
#     #num = cardsCount[flag]
#     if idx > cardsIdentity[flag-1]:
#         return length+flag
#     else: flag -= 1
        


# static
allCombinations = getAllCombinations()

# static
allSingles = np.array(tuple(cardsFrom((i, 1)) for i in range(0, 15)))
arrayallCombinations = np.array(getAllCombinations())


# import time
# lmw1=[]
# old1=[]

# time1 = time.time()
# for i in arrayallCombinations:
#     num = _B_cardsCount(i)
#     old1.append(num)
# time1end = time.time()-time1

# time2 = time.time()
# for i in arrayallCombinations:
#     num = _B_cardsCountlmw(i)
#     lmw1.append(num)
# time2end = time.time()-time2

# print(time1end,time2end)