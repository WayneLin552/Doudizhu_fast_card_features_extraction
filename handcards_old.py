############################################################################################
#  BLACK-JOKER RED-JOKER TWO THREE FOUR FIVE SIX SEVEN EIGHT NINE TEN JACK QUEEN KING ACE  #
############################################################################################

from combinations_old import allCombinations
from collections import Counter

# static
allSingles = (
    (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),#大王
    (0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),#小王
    (0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0),#2
    (0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),#Q
    (0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),#K
    (0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),#J
    (0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0),#3
    (0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1)
)

def leq(cardsA, cardsB): #位与位判断，大返回False 小返回True
    for a, b in zip(cardsA, cardsB):
        if a > b:
            return False
    return True

def subtract(cardsA, cardsB):#位与位相减
    return tuple(a - b for a, b in zip(cardsA, cardsB))

def decomposeTight(handInitial):#深度优先搜索的方法，由大到小
    combinations = tuple(c for c in allCombinations if leq(c, handInitial))#找出现手牌存在的所有出牌法
    singles = tuple(allSingles[i] for i in range(0, 15) if handInitial[i] > 0)#非空的牌号
    lenSingles = len(singles)
    idxSingles = [None] * 15
    m = 0
    for i in range(0, 15):
        if handInitial[i] > 0:
            idxSingles[i] = m
            m += 1
    idxSingles = tuple(idxSingles)
    #
    history = []
    result = tuple([] for i in range(0, 21))#最多最多20手打完牌
    def dfs(hand, i):
        flag = False
        while (i >= 0):
            if leq(combinations[i], hand): #手牌中含有这个组合 combination是升序，所以最后一个手牌扣的最多
                flag = True
                history.append(i + lenSingles)
                dfs(subtract(hand, combinations[i]), i)
                history.pop()
            i -= 1
        if not flag:
            for c in combinations:
                if leq(c, hand): #判断目前手牌还有没有出法，剩下的单牌
                    return
            s = reversed(tuple(idxSingles[i] for i, n in enumerate(hand) for x in range(0, n)))#找出单牌的牌号idx
            result[len(history) + sum(hand)].append(tuple(history) + tuple(s))#打完牌的最低次数以及出牌日志
    dfs(handInitial, len(combinations) - 1)#深度优先搜索，手牌+存在组合数-1
    return result, (singles + combinations)

def handcards_trans(handcards):
    cards_dict = Counter(handcards)
    result = []
    for i in [20,30,17,3,4,5,6,7,8,9,10,11,12,13,14]:
        try:
            result.append(cards_dict[i])
        except:
            result.append(0)
    return result


def decomposeLoose(handInitial):#深度优先遍历，由小到大
    handInitial = handcards_trans(handInitial)
    combinations = tuple(c for c in allCombinations if leq(c, handInitial))#找出所有可行的出牌
    singles = tuple(allSingles[i] for i in range(0, 15) if handInitial[i] > 0)#存在的牌类型
    lenSingles = len(singles)
    idxSingles = [None] * 15
    m = 0
    for i in range(0, 15):
        if handInitial[i] > 0:
            idxSingles[i] = m
            m += 1
    idxSingles = tuple(idxSingles)
    #
    history = []
    result = tuple([] for i in range(0, 21))
    def dfs(hand, i):
        while (i >= 0):
            if leq(combinations[i], hand):
                history.append(i + lenSingles)
                #dfs(subtract(hand, combinations[i]),i-1)
                dfs(subtract(hand, combinations[i]), i)
                history.pop()
            i -= 1
        s = reversed(tuple(idxSingles[i] for i, n in enumerate(hand) for x in range(0, n)))
        result[len(history) + sum(hand)].append(tuple(history) + tuple(s))
    dfs(handInitial, len(combinations) - 1)
    # a,b = result
    tmp = [len(x)>0 for x in result]
    min_play_times = tmp.index(True)
    return min_play_times
    # return result, (singles + combinations)



def decomposeLoose_lmw(handInitial):#深度优先遍历，由小到大
    combinations = tuple(c for c in allCombinations if leq(c, handInitial))#找出所有可行的出牌
    singles = tuple(allSingles[i] for i in range(0, 15) if handInitial[i] > 0)#存在的牌类型
    lenSingles = len(singles)
    idxSingles = [None] * 15
    m = 0
    for i in range(0, 15):
        if handInitial[i] > 0:
            idxSingles[i] = m
            m += 1
    idxSingles = tuple(idxSingles)
    #
    history = []
    result = tuple([] for i in range(0, 21))
    def dfs(hand, i):
        while (i >= 0):
            if leq(combinations[i], hand):
                history.append(i + lenSingles)
                dfs(subtract(hand, combinations[i]),i-1)
                #dfs(subtract(hand, combinations[i]), i)
                history.pop()
            i -= 1
        s = reversed(tuple(idxSingles[i] for i, n in enumerate(hand) for x in range(0, n)))
        result[len(history) + sum(hand)].append(tuple(history) + tuple(s))
    dfs(handInitial, len(combinations) - 1)
    return result, (singles + combinations)



def printResult(result):
    for i, l in enumerate(result):
        print(str(i) + ':')
        for x in l:
            print(x)
        print()




# handA = [0, 0, 1, 0, 2, 1, 1, 1, 2, 0, 1, 4, 1, 3, 0]
# handcards = [6, 4, 4, 4, 17, 5, 10, 3, 8, 5, 7, 14, 14, 13, 17, 4, 12]
# # handB = (1, 1, 3, 0, 0, 2, 3, 2, 1, 1, 0, 1, 0, 1, 1)

#import time
#t1 = time.time()
# result = decomposeLoose(handcards)
#print(time.time()-t1)

