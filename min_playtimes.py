# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 15:17:37 2022

@author: tracy
"""

from collections import Counter
from decompose import decomposeLoose#,decomposeLoose_lmw
#from functools import reduce


def handcards_trans(handcards):
    cards_dict = Counter(handcards)
    result = []
    for i in [20,30,17,3,4,5,6,7,8,9,10,11,12,13,14]:
        try:
            result.append(cards_dict[i])
        except:
            result.append(0)
    return result

def trans_handcards(hlist):
    handcards = []
    tmp= [20,30,17,3,4,5,6,7,8,9,10,11,12,13,14]
    for i in range(len(hlist)):
        for j in range(hlist[i]):
            handcards.append(tmp[i])
    handcards.sort()
    return handcards

def gen_min_playtimes(handcards,add_times=0):
    #print(handcards)
    hlist = handcards_trans(handcards)
    #print(hlist)
    result = decomposeLoose(hlist)
    #print(result)
    a,b = result
    tmp = [len(x)>0 for x in a]
    #print(tmp)
    min_play_times = tmp.index(True)
    #print(min_play_times)
    # actions = set()
    # for i in range(min_play_times,min_play_times+add_times+1):
    #     if len(a[i])>0:
    #         actions = actions | set(reduce(lambda x, y: set(x)|set(y), a[i]))
        
    # actions_list = [trans_handcards(b[x]) for x in actions]
    # return actions_list
    return min_play_times

def gen_min_playtimes_lmw(handcards,add_times=0):
    #print(handcards)
    hlist = handcards_trans(handcards)
    #print(hlist)
    result = decomposeLoose_lmw(hlist)
    #print(result)
    a,b = result
    tmp = [len(x)>0 for x in a]
    #print(tmp)
    min_play_times = tmp.index(True)
    #print(min_play_times)
    # actions = set()
    # for i in range(min_play_times,min_play_times+add_times+1):
    #     if len(a[i])>0:
    #         actions = actions | set(reduce(lambda x, y: set(x)|set(y), a[i]))
        
    # actions_list = [trans_handcards(b[x]) for x in actions]
    # return actions_list
    return min_play_times


#####################1####################
# import time
# # handcards = [3,3,3,4,4,5,7,8,9,10,14,14,20] #3-k分别是3-13，A是14,2是17，小王是20，大王是30
# handcards = [10, 12, 8, 7, 6, 7, 4, 5, 6, 9, 30, 6, 4, 8, 13, 9, 4]
# time1 = time.time()
# mintime=gen_min_playtimes(handcards)
# print(time.time()-time1)
# print('min_time:',mintime)

#####################2####################
#time2 = time.time()
#mintime2=gen_min_playtimes_lmw(handcards)
#print(time.time()-time2)
#print('min_time:',mintime2)