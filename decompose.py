############################################################################################
#  BLACK-JOKER RED-JOKER TWO THREE FOUR FIVE SIX SEVEN EIGHT NINE TEN JACK QUEEN KING ACE  #
############################################################################################

from cards import allSingles, allCombinations, arrayallCombinations, cardsFrom, cardsFrom_old, cardsCount, cardsGrEq, cardsSubtract

import time

def timer(func):
    def wrapped(*args, **kwargs):
        ts = time.time()
        res = func(*args, **kwargs)
        te = time.time()
        print(te - ts)
        return res
    return wrapped

def getFeasibility(handInitial):
    combinations = tuple(c for c in allCombinations if cardsGrEq(handInitial, c))
    singles = tuple(s for s in allSingles if cardsGrEq(handInitial, s))
    return combinations, singles, len(singles)


#@timer

def decomposeMin(handInitial):
    combinations, singles, lenSingles = getFeasibility(handInitial)
    #
    history = []
    result = []
    minCountL = [21]
    def dfs(hand, i):
        lenHistory = len(history)
        sumHand = cardsCount(hand)
        flag = False
        while (i >= 0):
            if lenHistory >= minCountL[0] and sumHand > 0:
                return
            ci = combinations[i]
            if cardsGrEq(hand, ci):
                flag = True
                history.append(i + lenSingles)
                # retry ith because `hand` may have multiple instances of the same combination
                dfs(cardsSubtract(hand, ci), i)
                history.pop()
            i -= 1
        if not flag:
            # exhausted
            minCount = minCountL[0]
            newCount = lenHistory + sumHand
            if newCount > minCount:
                return
            
            for c in combinations:
                if cardsGrEq(hand, c):
                    return
            # succeed
            
            if newCount < minCount:
                minCountL[0] = newCount
                result.clear()
            # now there are no duplicates in `hand`
            # l = []
            # for i, single in enumerate(allSingles):
            #     if cardsGrEq(hand, single):
            #         l.append(i)
            # result.append(tuple(history) + tuple(l))

    dfs(handInitial, len(combinations) - 1)


    #return result, (singles + combinations), minCountL[0]

    return minCountL[0]


def decomposeMinest(handInitial):
    time1= time.time()
    combinations = arrayallCombinations[handInitial & arrayallCombinations == arrayallCombinations]
    time1end = time.time()-time1
    print(time1end)
    print(len(combinations))
    #
    history = []
    minCountL = [21]
    def dfs(hand, i):
        lenHistory = len(history)
        sumHand = cardsCount(hand)
        flag = False
        while (i >= 0):
            if lenHistory >= minCountL[0] and sumHand > 0:
                return
            #ci = combinations[i]
            if (hand & combinations[i] == combinations[i]):
                flag = True
                history.append(1)
                # retry ith because `hand` may have multiple instances of the same combination
                dfs(cardsSubtract(hand, int(combinations[i])), i-1)
                history.pop()
            i -= 1
        if not flag:
            # exhausted
            minCount = minCountL[0]
            newCount = lenHistory + sumHand
            if newCount > minCount:
                return
            
            if (hand & combinations == combinations).any():
            #for c in combinations:
            #    if cardsGrEq(hand, c):
                return
            # succeed
            
            if newCount < minCount:
                minCountL[0] = newCount
    time2 = time.time()
    dfs(handInitial, len(combinations) - 1)
    time2end = time.time()-time2
    print(time2end)
    print(time1end+time2end,'\n')
    return minCountL[0]


#@timer
def decomposeTight(handInitial):
    # combinations, singles, lenSingles = feasibility
    combinations, singles, lenSingles = getFeasibility(handInitial)
    #
    history = []
    result = tuple([] for _ in range(0, 21))
    def dfs(hand, i):
        flag = False
        while (i >= 0):
            ci = combinations[i]
            if cardsGrEq(hand, ci):
                flag = True
                history.append(i + lenSingles)
                dfs(cardsSubtract(hand, ci), i)
                history.pop()
            i -= 1
        if not flag:
            for c in combinations:
                if cardsGrEq(hand, c):
                    return
            # now there are no duplicates in `hand`
            l = []
            for i, single in enumerate(allSingles):
                if cardsGrEq(hand, single):
                    l.append(i)
            result[len(history) + len(l)].append(tuple(history) + tuple(l))
    dfs(handInitial, len(combinations) - 1)
    return result, (singles + combinations)


#@timer
def decomposeLoose(handInitial):
    combinations, singles, lenSingles = getFeasibility(handInitial)
    # combinations, singles, lenSingles = feasibility
    #
    history = []
    result = tuple([] for _ in range(0, 21))
    def dfs(hand, i):
        while (i >= 0):
            ci = combinations[i]
            if cardsGrEq(hand, ci):
                history.append(i + lenSingles)
                dfs(cardsSubtract(hand, ci), i)
                history.pop()
            i -= 1
        l = []
        for i, single in enumerate(allSingles):
            tmp = hand
            while cardsGrEq(tmp, single):
                l.append(i)
                tmp = cardsSubtract(tmp, single)
        result[len(history) + len(l)].append(tuple(history) + tuple(l))
    dfs(handInitial, len(combinations) - 1)
    a,b = result
    tmp = [len(x)>0 for x in a]
    min_play_times = tmp.index(True)
    return min_play_times


def printResult(result):
    for i, l in enumerate(result):
        print(str(i) + ':')
        for x in l:
            print(x)
        print()



handA = cardsFrom((2, 1), (4, 2), (5, 1), (6, 1), (7, 1), (8, 2), (10, 1), (11, 4), (12, 1), (13, 3))
handB = cardsFrom((0, 1), (1, 1), (2, 3), (5, 2), (6, 3), (7, 2), (8, 1), (9, 1), (11, 1), (13, 1), (14, 1))
