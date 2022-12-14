# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 20:07:10 2022

@author: LinMouwei
"""

from cards import arrayallCombinations, cardsFrom, cardsCount, cardsSubtract
from collections import Counter

def card_trans(orihandcards):
    # replace_dict={'1':3, '2':4, '3':5, \
    #                 '4':6, '5':7, '6':8, '7':9, '8':10, '9':11, '10':12, '11':13, \
    #                 '12':14, '13':2, '14':0, '15':1}
    replace_dict = {17:2,20:0,30:1}
    r_x=[replace_dict[i] if i in replace_dict else i for i in orihandcards]
    a = Counter(r_x)
    try:
        return cardsFrom(*a.items())
    except:
        return 1

def getFeasibility(handInitial):
    combinations = arrayallCombinations[handInitial & arrayallCombinations == arrayallCombinations]
    # singles = allSingles[handInitial & allSingles == allSingles]
    return combinations

def get_min_playhands(handInitial):
    combinations = getFeasibility(handInitial)
    history = []
    minCountL = [21]
    def dfs(hand, i):
        lenHistory = len(history)
        sumHand = cardsCount(hand)
        flag = False
        while (i >= 0):
            if lenHistory >= minCountL[0] and sumHand > 0:
                return
            if (hand & combinations[i] == combinations[i]):
                flag = True
                history.append(1)
                dfs(cardsSubtract(hand, int(combinations[i])), i-1)
                history.pop()
            i -= 1
        if not flag:
            minCount = minCountL[0]
            newCount = lenHistory + sumHand
            if newCount > minCount:
                return
            
            if (hand & combinations == combinations).any():
            #for c in combinations:
            #    if cardsGrEq(hand, c):
                return
            if newCount < minCount:
                minCountL[0] = newCount
    dfs(handInitial, len(combinations) - 1)
    return minCountL[0]


###################################################
import copy
from move_generator import MovesGener

def BiggerList(x,y): 
    if len(x)==0 and len(y)==0:
        return x
    elif len(x)*len(y)>0:
        if x[-1]>=y[-1]:
            return x
        else:
            return y
    elif len(x)==0:
        return y
    else:
        return x

def GetSet(x):
    return [i[0] for i in x]

def GetSet1(x):
    return [i[-1] for i in x]

def fenlei(a):
    list_5 = []
    list_6 = []
    list_7 = []
    list_other = []
    for i in a:
        if len(i) == 5:
            list_5.append(i)
        elif len(i) == 6:
            list_6.append(i)
        elif len(i) == 7:
            list_7.append(i)
        else:
            list_other.append(i)
    return list_5,list_6,list_7,list_other

def fenlei_1(a):
    list_3 = []
    list_4 = []
    list_5 = []
    list_other = []
    for i in a:
        if len(i) == 6:
            list_3.append(i)
        elif len(i) == 8:
            list_4.append(i)
        elif len(i) == 10:
            list_5.append(i)
        else:
            list_other.append(i)
    return list_3,list_4,list_5,list_other

def fenlei_2(a):
    list_2 = []
    list_3 = []
    list_4 = []
    list_other = []
    for i in a:
        if len(i) == 6:
            list_2.append(i)
        elif len(i) == 9:
            list_3.append(i)
        elif len(i) == 12:
            list_4.append(i)
        else:
            list_other.append(i)
    return list_2,list_3,list_4,list_other

def fenlei_3(a):
    list_2 = []
    list_3 = []
    list_other = []
    for i in a:
        if len(i) == 10:
            list_2.append(i)
        elif len(i) == 15:
            list_3.append(i)
        else:
            list_other.append(i)
    return list_2, list_3, list_other


def qudanzhi(a):
    a=[]
    for i in a:
        if i[0]==i[2]:
            a.append(i[0])
        if i[2]==i[4]:
            a.append(i[2])
        if i[4]==i[6]:
            a.append(i[4])
    return list(set(a))
    

def qudanzhi3(a): 
    b=[]
    for i in a:
        if i[0]==i[2]:
            b.append(i[0])
        elif i[2]==i[4]:
            b.append(i[2])
        elif i[4]==i[6]:
            b.append(i[4])
        else:
            b.append(i[6])
    return list(set(b))

def quzuihou(a):
    return [i[-1] for i in a]

def sort_single(nn,aa,bb): #???????????? ????????????1-11 ????????????12-22 ????????????23-33
    list1=[0]*11
    list2=[0]*11
    list3=[0]*11
    # lists=[0]*33
    n=list(set(nn))
    a=list(set(aa))
    b=list(set(bb))
    # allone = [[0,j] for j in n]
    # allone += [[1,j] for j in a]
    # allone += [[2,j] for j in b]
    # allone = sorted(allone, key=lambda x:x[1])
    # length = len(allone)
    # if length >= 10:
    #     for j in range(10):
    #         lists[allone[j][0]*11+j] = 1
    # else:
    #     for j in range(length):
    #         lists[allone[j][0]*11+j] = 1
    # if len(n) > 10:
    #     lists[10] = 1
    # if len(a) > 10:
    #     lists[21] = 1
    # if len(b) > 10:
    #     lists[32] = 1
    for j in range(10):
        x=BiggerList(n,a)
        x=copy.copy(BiggerList(x,b))
        if x!=[]:
            if n!=[]:
                if  x[-1]==n[-1]:
                    list1[j]=1
                    n.pop()

            if b!=[]:
                if  x[-1]==b[-1]:
                    list3[j]=1
                    b.pop()

            if a!=[]:
                if x[-1]==a[-1]:
                    list2[j]=1
                    a.pop()
                    
    if n!=[]:
        list1[-1]=1
    if b!=[]:
        list3[-1]=1
    if a!=[]:
        list2[-1]=1
    return list1,list2,list3
    # return lists[:11], lists[11:22], lists[22:]
    

def sort_double(n,a,b): #????????????  ????????????34-44 ??????45-55 ??????56-66
    mg1=MovesGener(n)
    nn=mg1.gen_type_2_pair()
    nnd=GetSet(nn)
    mg2=MovesGener(b)
    bb=mg2.gen_type_2_pair()
    bbd=GetSet(bb)
    mg3=MovesGener(a)
    aa=mg3.gen_type_2_pair()
    aad=GetSet(aa)
    list1=[0]*11
    list2=[0]*11
    list3=[0]*11
    for j in range(10):
        x=BiggerList(nnd,bbd)
        x=copy.copy(BiggerList(x,aad))
        if x!=[]:
            if nnd!=[]:  #x?????? n???
                if x[-1]==nnd[-1]:
                    list1[j]=1
                    nnd.pop()

            if bbd!=[]:
                if x[-1]==bbd[-1]:
                    list3[j]=1
                    bbd.pop()

            if aad!=[]:
                if x[-1]==aad[-1]:
                    list2[j]=1
                    aad.pop()                       
    if nnd!=[]:
        list1[-1]=1
    if bbd!=[]:
        list3[-1]=1
    if aad!=[]:
        list2[-1]=1
    return list1,list2,list3

def sort_triple(n,a,b): #???????????? ??????67-72 ??????73-78 ??????79-84 
    mg1=MovesGener(n)
    nn=mg1.gen_type_3_triple()
    nnd=GetSet(nn)
    mg2=MovesGener(b)
    bb=mg2.gen_type_3_triple()
    bbd=GetSet(bb)
    mg3=MovesGener(a)
    aa=mg3.gen_type_3_triple()
    aad=GetSet(aa)
    list1=[0]*6
    list2=[0]*6
    list3=[0]*6
    
    for j in range(5):
        x=BiggerList(nnd,bbd)
        x=copy.copy(BiggerList(x,aad))
        if x!=[]:
            if nnd!=[]:  #x?????? n???
                if x[-1]==nnd[-1]:
                    list1[j]=1
                    nnd.pop()
                    

            if bbd!=[]:
                if x[-1]==bbd[-1]:
                    list3[j]=1
                    bbd.pop()
                    

            if aad!=[]:
                if  x[-1]==aad[-1]:
                    list2[j]=1
                    aad.pop()

    if nnd!=[]:
        list1[-1]=1
    if bbd!=[]:
        list3[-1]=1
    if aad!=[]:
        list2[-1]=1
    return list1,list2,list3

def sort_3plus1(n,a,b): #??????????????? ??????85-90 ??????91-96 ??????97-102
    mg1=MovesGener(n)
    nn=mg1.gen_type_6_3_1()
    nnd=GetSet1(nn)
    nnd=list(set(nnd))
    mg2=MovesGener(b)
    bb=mg2.gen_type_6_3_1()
    bbd=GetSet1(bb)
    bbd=list(set(bbd))
    mg3=MovesGener(a)
    aa=mg3.gen_type_6_3_1()
    aad=GetSet1(aa)
    aad=list(set(aad))
    list1=[0]*6
    list2=[0]*6
    list3=[0]*6

    for j in range(5):
        x=BiggerList(nnd,bbd)
        x=copy.copy(BiggerList(x,aad))
        if x!=[]:
            if nnd!=[]:  #x?????? n???
                if x[-1]==nnd[-1]:
                    list1[j]=1
                    nnd.pop()
                    

            if bbd!=[]:
                if x[-1]==bbd[-1]:
                    list3[j]=1
                    bbd.pop()
                    

            if aad!=[]:
                if  x[-1]==aad[-1]:
                    list2[j]=1
                    aad.pop()

    if nnd!=[]:
        list1[-1]=1
    if bbd!=[]:
        list3[-1]=1
    if aad!=[]:
        list2[-1]=1
    return list1,list2,list3

# ?????? ????????????????????????????????? 103-115 ??????116-128 ??????129-141
def sort_serial_single(n,a,b):
    mgn = MovesGener(n)
    mgb = MovesGener(b)
    mga = MovesGener(a)
    n_single_move = mgn.gen_type_8_serial_single()
    b_single_move = mgb.gen_type_8_serial_single()
    a_single_move = mga.gen_type_8_serial_single()
    n_list_5,n_list_6,n_list_7,n_list_other=fenlei(n_single_move)
    a_list_5,a_list_6,a_list_7,a_list_other=fenlei(a_single_move)
    b_list_5,b_list_6,b_list_7,b_list_other=fenlei(b_single_move)
    list1=[0]*4 #1-9 ??????567 ??????567 ??????567
    list2=[0]*4
    list3=[0]*5
    list4=[0]*4
    list5=[0]*4
    list6=[0]*5
    list7=[0]*4
    list8=[0]*4
    list9=[0]*5
    if n_list_other != []:
        list3[-1]=1
    if b_list_other != []:
        list9[-1]=1
    if a_list_other != []:
        list6[-1]=1
    n_list_5_1 = quzuihou(n_list_5)
    b_list_5_1=quzuihou(b_list_5)
    a_list_5_1=quzuihou(a_list_5)
    n_list_6_1=quzuihou(n_list_6)
    b_list_6_1=quzuihou(b_list_6)
    a_list_6_1=quzuihou(a_list_6)
    n_list_7_1=quzuihou(n_list_7)
    b_list_7_1=quzuihou(b_list_7)
    a_list_7_1=quzuihou(a_list_7)
    for j in range(3): 
        x = BiggerList(n_list_5_1, b_list_5_1)
        x = copy.copy(BiggerList(x, a_list_5_1))
        if x != []:
            if n_list_5_1 != []:  # x?????? n???
                if  x[-1] == n_list_5_1[-1]:
                    list1[j]=1
                    n_list_5_1.pop()

            if b_list_5_1 != []:
                if  x[-1] == b_list_5_1[-1]:
                    list7[j]=1
                    b_list_5_1.pop()

            if a_list_5_1 != []:
                if  x[-1] == a_list_5_1[-1]:
                    list4[j]=1
                    a_list_5_1.pop()

    if n_list_5_1 != []:
        list1[-1]=1
    if b_list_5_1 != []:
        list7[-1]=1
    if a_list_5_1 != []:
        list4[-1]=1
    for j in range(3):
        x = BiggerList(n_list_7_1, b_list_7_1)
        x = copy.copy(BiggerList(x, a_list_7_1))
        if x != []:
            if n_list_7_1 != []:  # x?????? n???
                if  x[-1] == n_list_7_1[-1]:
                    list3[j]=1
                    n_list_7_1.pop()

            if b_list_7_1 != []:
                if x[-1] == b_list_7_1[-1]:
                    list9[j]=1
                    b_list_7_1.pop()

            if a_list_7_1 != []:
                if x[-1] == a_list_7_1[-1]:
                    list6[j]=1
                    a_list_7_1.pop()

    if n_list_7_1 != []:
        list3[-2]=1
    if b_list_7_1 != []:
        list9[-2]= 1
    if a_list_7_1 != []:
        list6[-2]=1
    for j in range(3):
        x = BiggerList(n_list_6_1, b_list_6_1)
        x = copy.copy(BiggerList(x, a_list_6_1))
        if x != []:
            if n_list_6_1 != []:  # x?????? n???
                if x[-1] == n_list_6_1[-1]:
                    list2[j]=1
                    n_list_6_1.pop()

            if b_list_6_1 != []:
                if  x[-1] == b_list_6_1[-1]:
                    list8[j]=1
                    b_list_6_1.pop()

            if a_list_6_1 != []:
                if x[-1] == a_list_6_1[-1]:
                    list5[j]=1
                    a_list_6_1.pop()

    if n_list_6_1 != []:
        list2[-1]=1
    if b_list_6_1 != []:
        list8[-1]=1
    if a_list_6_1 != []:
        list5[-1]=1
    return list1+list2+list3,list4+list5+list6,list7+list8+list9

#?????? ????????????????????? 142-154 ?????????????????????155-167 ?????????????????????168-180
def sort_serial_pair(n,a,b):
    mgn = MovesGener(n)
    mgb = MovesGener(b)
    mga = MovesGener(a)
    n_pair_move=mgn.gen_type_9_serial_pair()
    b_pair_move=mgb.gen_type_9_serial_pair()
    a_pair_move=mga.gen_type_9_serial_pair()
    n_list_3,n_list_4,n_list_5,n_list_other=fenlei_1(n_pair_move)
    b_list_3,b_list_4,b_list_5,b_list_other=fenlei_1(b_pair_move)
    a_list_3,a_list_4,a_list_5,a_list_other=fenlei_1(a_pair_move)
    list1=[0]*4 
    list2=[0]*4
    list3=[0]*5
    list4=[0]*4
    list5=[0]*4
    list6=[0]*5
    list7=[0]*4
    list8=[0]*4
    list9=[0]*5
    if n_list_other != []:
        list3[-1]=1
    if b_list_other != []:
        list9[-1]=1
    if a_list_other != []:
        list6[-1]=1
    n_list_3_1=quzuihou(n_list_3)
    n_list_4_1=quzuihou(n_list_4)
    n_list_5_1=quzuihou(n_list_5)
    b_list_3_1=quzuihou(b_list_3)
    b_list_4_1=quzuihou(b_list_4)
    b_list_5_1=quzuihou(b_list_5)
    a_list_3_1=quzuihou(a_list_3)
    a_list_4_1=quzuihou(a_list_4)
    a_list_5_1=quzuihou(a_list_5)
    for j in range(3):
        x = BiggerList(n_list_3_1, b_list_3_1)
        x = copy.copy(BiggerList(x, a_list_3_1))
        if x != []:
            if n_list_3_1 != []:  # x?????? n??????
                if x[-1] == n_list_3_1[-1]:
                    list1[j]=1
                    n_list_3_1.pop()

            if b_list_3_1 != []:
                if  x[-1] == b_list_3_1[-1]:
                    list7[j]=1
                    b_list_3_1.pop()

            if a_list_3_1 != []:
                if x[-1] == a_list_3_1[-1]:
                    list4[j]=1
                    a_list_3_1.pop()

    if n_list_3_1 != []:
        list1[-1]=1
    if b_list_3_1 != []:
        list7[-1]=1
    if a_list_3_1 != []:
        list4[-1]=1
    for j in range(3):
        x = BiggerList(n_list_4_1, b_list_4_1)
        x = copy.copy(BiggerList(x, a_list_4_1))
        if x != []:
            if n_list_4_1 != []:  # x?????? n??????
                if x[-1] == n_list_4_1[-1]:
                    list2[j]=1
                    n_list_4_1.pop()

            if b_list_4_1 != []:
                if  x[-1] == b_list_4_1[-1]:
                    list8[j]=1
                    b_list_4_1.pop()

            if a_list_4_1 != []:
                if x[-1] == a_list_4_1[-1]:
                    list5[j]=1
                    a_list_4_1.pop()

    if n_list_4_1 != []:
        list2[-1]=1
    if b_list_4_1 != []:
        list8[-1]=1
    if a_list_4_1 != []:
        list5[-1]=1
    for j in range(3):
        x = BiggerList(n_list_5_1, b_list_5_1)
        x = copy.copy(BiggerList(x, a_list_5_1))
        if x != []:
            if n_list_5_1 != []:  # x?????? n??????
                if x[-1] == n_list_5_1[-1]:
                    list3[j]=1
                    n_list_5_1.pop()

            if b_list_5_1 != []:
                if  x[-1] == b_list_5_1[-1]:
                    list9[j]=1
                    b_list_5_1.pop()

            if a_list_5_1 != []:
                if x[-1] == a_list_5_1[-1]:
                    list6[j]=1
                    a_list_5_1.pop()

    if n_list_5_1 != []:
        list3[-2]=1
    if b_list_5_1 != []:
        list9[-2]=1
    if a_list_5_1 != []:
        list6[-2]=1
    return list1+list2+list3,list4+list5+list6,list7+list8+list9

def sort_serial_triple(n,a,b): #????????????????????? 181-193 ??????194-206 ??????207-219
    mgn = MovesGener(n)
    mgb = MovesGener(b)
    mga = MovesGener(a)
    n_triple_move=mgn.gen_type_10_serial_triple()
    b_triple_move=mgb.gen_type_10_serial_triple()
    a_triple_move=mga.gen_type_10_serial_triple()
    n_list_2,n_list_3,n_list_4,n_list_other=fenlei_2(n_triple_move)
    b_list_2,b_list_3,b_list_4,b_list_other=fenlei_2(b_triple_move)
    a_list_2,a_list_3,a_list_4,a_list_other=fenlei_2(a_triple_move)
    
    list1=[0]*4 
    list2=[0]*4
    list3=[0]*4
    list4=[0]*4
    list5=[0]*4
    list6=[0]*4
    list7=[0]*4
    list8=[0]*4
    list9=[0]*4

    n_list_2_1=quzuihou(n_list_2)
    n_list_3_1=quzuihou(n_list_3)
    n_list_4_1=quzuihou(n_list_4)
    b_list_2_1=quzuihou(b_list_2)
    b_list_3_1=quzuihou(b_list_3)
    b_list_4_1=quzuihou(b_list_4)
    a_list_2_1=quzuihou(a_list_2)
    a_list_3_1=quzuihou(a_list_3)
    a_list_4_1=quzuihou(a_list_4)
    
    for j in range(3): #????????????
        x = BiggerList(n_list_3_1, b_list_3_1)
        x = copy.copy(BiggerList(x, a_list_3_1))
        if x != []:
            if n_list_3_1 != []:  # x?????? n???
                if  x[-1] == n_list_3_1[-1]:
                    list2[j]=1
                    n_list_3_1.pop()

            if b_list_3_1 != []:
                if  x[-1] == b_list_3_1[-1]:
                    list8[j]=1
                    b_list_3_1.pop()

            if a_list_3_1 != []:
                if  x[-1] == a_list_3_1[-1]:
                    list5[j]=1
                    a_list_3_1.pop()
    if n_list_3_1 != []:
        list2[-1]=1
    if b_list_3_1 != []:
        list8[-1]=1
    if a_list_3_1 != []:
        list5[-1]=1
        
    for j in range(3): #????????????
        x = BiggerList(n_list_4_1, b_list_4_1)
        x = copy.copy(BiggerList(x, a_list_4_1))
        if x != []:
            if n_list_4_1 != []:  # x?????? n???
                if  x[-1] == n_list_4_1[-1]:
                    list3[j]=1
                    n_list_4_1.pop()

            if b_list_4_1 != []:
                if  x[-1] == b_list_4_1[-1]:
                    list9[j]=1
                    b_list_4_1.pop()

            if a_list_4_1 != []:
                if  x[-1] == a_list_4_1[-1]:
                    list6[j]=1
                    a_list_4_1.pop()
    if n_list_4_1 != []:
        list3[-1]=1
    if b_list_4_1 != []:
        list9[-1]=1
    if a_list_4_1 != []:
        list6[-1]=1
        
    for j in range(3): #????????????
        x = BiggerList(n_list_2_1, b_list_2_1)
        x = copy.copy(BiggerList(x, a_list_2_1))
        if x != []:
            if n_list_2_1 != []:  # x?????? n???
                if  x[-1] == n_list_2_1[-1]:
                    list1[j]=1
                    n_list_2_1.pop()

            if b_list_2_1 != []:
                if  x[-1] == b_list_2_1[-1]:
                    list7[j]=1
                    b_list_2_1.pop()

            if a_list_2_1 != []:
                if  x[-1] == a_list_2_1[-1]:
                    list4[j]=1
                    a_list_2_1.pop()
    if n_list_2_1 != []:
        list1[-1]=1
    if b_list_2_1 != []:
        list7[-1]=1
    if a_list_2_1 != []:
        list4[-1]=1
    return list1+list2+list3,list4+list5+list6,list7+list8+list9

def sort_boom(n,a,b): #???????????? ????????????220-213 ??????214-217 ??????218-221
    mg1=MovesGener(n)
    nnn=mg1.gen_type_4_bomb()
    nnd=GetSet(nnn)
    mg2=MovesGener(b)
    bbb=mg2.gen_type_4_bomb()
    bbd=GetSet(bbb)
    mg3=MovesGener(a)
    aaa=mg3.gen_type_4_bomb()
    aad=GetSet(aaa)
    list1=[0]*4
    list2=[0]*4
    list3=[0]*4
    
    for j in range(3):
        x=copy.deepcopy(BiggerList(nnd,bbd))
        x=copy.deepcopy(BiggerList(x,aad))
        if x!=[]:
            if nnd!=[]:  #x?????? n???
                if x[-1]==nnd[-1]:
                    list1[j]=1
                    nnd.pop()
                   

            if bbd!=[]:
                if x[-1]==bbd[-1]:
                    list3[j]=1
                    bbd.pop()
                    

            if aad!=[]:
                if  x[-1]==aad[-1]:
                    list2[j]=1
                    aad.pop()

    if nnd!=[]:
        list1[-1]=1
    if bbd!=[]:
        list3[-1]=1
    if aad!=[]:
        list2[-1]=1
    return list1,list2,list3

def sort_4plus2(n,a,b): #??????????????? ?????? 222-235 ??????236-239 ??????240-243
    mg1=MovesGener(n)
    nn=mg1.gen_type_13_4_2()
    nnd=GetSet(nn)
    nnd=list(set(nnd))
    mg2=MovesGener(b)
    bb=mg2.gen_type_13_4_2()
    bbd=GetSet(bb)
    bbd=list(set(bbd))
    mg3=MovesGener(a)
    aa=mg3.gen_type_13_4_2()
    aad=GetSet(aa)
    aad=list(set(aad))
    list1=[0]*4
    list2=[0]*4
    list3=[0]*4

    for j in range(3):
        x=BiggerList(nnd,bbd)
        x=copy.copy(BiggerList(x,aad))
        if x!=[]:
            if nnd!=[]:  #x?????? n???
                if x[-1]==nnd[-1]:
                    list1[j]=1
                    nnd.pop()
                    

            if bbd!=[]:
                if x[-1]==bbd[-1]:
                    list3[j]=1
                    bbd.pop()
                    

            if aad!=[]:
                if x[-1]==aad[-1]:
                    list2[j]=1
                    aad.pop()

    if nnd!=[]:
        list1[-1]=1
    if bbd!=[]:
        list3[-1]=1
    if aad!=[]:
        list2[-1]=1
    return list1,list2,list3

def sort_20_30(n,a,b): #????????????????????????????????? ????????????244-245 ??????246-247 ??????248-249
    list1=[0]*2
    list2=[0]*2
    list3=[0]*2
    if 20 in n and 30 in n:
        list1[0]=1
    if 20 in b and 30 in b:
        list3[0]=1
    if 20 in a and 30 in a:
        list2[0]=1
    if 20 in n or 30 in n:
        list1[0]=1
    if 20 in b or 30 in b:
        list3[0]=1
    if 20 in a or 30 in a:
        list2[0]=1
    return list1,list2,list3

def leave_card_num(nn,aa,bb): #????????????????????? ???????????? 250-260 ??????261-271 ??????272-282
    x = len(nn)
    y = len(bb)
    z = len(aa)
    list1=[0]*11
    list2=[0]*11
    list3=[0]*11
    if x != 0 and x<=10:
        list1[x-1]=1
    if x > 10:
        list1[-1]=1
    if y != 0 and y<=10:
        list3[y-1]=1
    if y > 10:
        list3[-1]=1
    if z != 0 and z<=10:
        list2[z-1]=1
    if z > 10:
        list2[-1]=1
    return list1,list2,list3 

def brother(up,down): #down????????????role #??????????????????283 ??????????????????284 1????????????0?????????
    list1 = []
    list2 = []
    list1.append(abs(up-down)*up) #0??????????????????1???????????????
    list2.append(abs(up-down)*down)
    list1=[0] #?????????????????????
    list2=[0] #?????????????????????
    return list1,list2

def sort_serial_triple_3_2(n,a,b): #??????????????????????????????????????? 285-293 ??????294-302 ??????303-311
    mgn = MovesGener(n)
    mgb = MovesGener(b)
    mga = MovesGener(a)
    n_triple_move = mgn.gen_type_12_serial_3_2()
    b_triple_move = mgb.gen_type_12_serial_3_2()
    a_triple_move = mga.gen_type_12_serial_3_2()
    n_list_2, n_list_3,  n_list_other = fenlei_3(n_triple_move)
    b_list_2, b_list_3,  b_list_other = fenlei_3(b_triple_move)
    a_list_2, a_list_3,  a_list_other = fenlei_3(a_triple_move)
    list1=[0]*4 #1-9 ??????23 ??????23 ??????23
    list2=[0]*5
    list3=[0]*4
    list4=[0]*5
    list5=[0]*4
    list6=[0]*5
    if n_list_other != []:
        list2[-1]=1
    if b_list_other != []:
        list6[-1]=1
    if a_list_other != []:
        list4[-1]=1
    n_list_2_1 = qudanzhi(n_list_2)
    n_list_3_1 = qudanzhi3(n_list_3)
    b_list_2_1 = qudanzhi(b_list_2)
    b_list_3_1 = qudanzhi3(b_list_3)
    a_list_2_1 = qudanzhi(a_list_2)
    a_list_3_1 = qudanzhi3(a_list_3)
    for j in range(3):
        x = copy.deepcopy(BiggerList(n_list_2_1, b_list_2_1))
        x = copy.deepcopy(BiggerList(x, a_list_2_1))
        if x != []:
            if n_list_2_1 != []:  # x?????? n???
                if  x[-1] == n_list_2_1[-1]:
                    list1[j]=1
                    n_list_2_1.pop()

            if b_list_2_1 != []:
                if x[-1] == b_list_2_1[-1]:
                    list5[j] = 1
                    b_list_2_1.pop()

            if a_list_2_1 == []:
                if x[-1] == a_list_2_1[-1]:
                    list3[j]=1
                    a_list_2_1.pop()
    if n_list_2_1 != []:
        list1[-1] = 1
    if b_list_2_1 != []:
        list5[-1] = 1
    if a_list_2_1 != []:
        list3[-1]= 1
    for j in range(3):
        x = copy.deepcopy(BiggerList(n_list_3_1, b_list_3_1))
        x = copy.deepcopy(BiggerList(x, a_list_3_1))
        if x != []:
            if n_list_3_1 != []:  # x?????? n???
                if  x[-1] == n_list_3_1[-1]:
                    list2[j]=1
                    n_list_3_1.pop()

            if b_list_3_1 != []:
                if x[-1] == b_list_3_1[-1]:
                    list6[j] = 1
                    b_list_3_1.pop()

            if a_list_3_1 != []:
                if x[-1] == a_list_3_1[-1]:
                    list4[j] = 1
                    a_list_3_1.pop()

    if n_list_3_1 != []:
        list2[-2] = 1
    if b_list_3_1 != []:
        list6[-2] = 1
    if a_list_3_1 != []:
        list4[-2] = 1
    return list1+list2,list3+list4,list5+list6


def min_shoushu1(n,a,b): #???????????? ????????????312-317 ??????318-323 ??????324-329
    

    # time21 = time.time()
    n_ss = get_min_playhands(card_trans(n))
    # time21end = time.time()-time21
    # time22 = time.time()
    b_ss = get_min_playhands(card_trans(b))
    # time22end = time.time()-time22
    # time23 = time.time()
    a_ss = get_min_playhands(card_trans(a))
    # time23end = time.time()-time23
    # print(time21end,time22end,time23end,time21end+time22end+time23end)
    list1=[0]*6
    list2=[0]*6
    list3=[0]*6
    if n_ss > 5:
        list1[-1] = 1
    else:
        list1[n_ss - 1]=1
    if b_ss > 5:
        list2[-1] = 1
    else:
        list2[b_ss - 1]=1
    if a_ss > 5:
        list3[-1] = 1
    else:
        list3[a_ss - 1]=1
    
    # if n_ss <= 5 and n_ss != 0:
    #     list1[n_ss-1]=1
    # elif n_ss > 5:
    #     list1[-1]=1
    # if b_ss <= 5 and b_ss != 0:
    #     list3[b_ss-1]=1
    # elif b_ss > 5:
    #     list3[-1]=1
    # if a_ss <= 5 and a_ss != 0:
    #     list2[a_ss-1]=1
    # elif a_ss > 5:
    #     list2[-1]=1
    return list1,list2,list3




def sortgenpai1(x): #????????????330-343
    list1=[0]*14     
    if x==[]:
        list1[-1]=1
    else:# x??????
        if 20 in x and 30 in x:
            list1[0]=1
        mg1=MovesGener(x)
        if len(x)==4 and mg1.gen_type_4_bomb() !=[]:
            list1[1]=1
        if len(x)==1:
            list1[2]=1
        if len(x)==2 and len(mg1.gen_type_2_pair())!=0:
            list1[3]=1
        if len(x)==3 and len(mg1.gen_type_3_triple())!=0:
            list1[4]=1
        if len(x)==4 and len(mg1.gen_type_6_3_1())!=0:
            list1[5]=1
        if len(x)==5 and len(mg1.gen_type_7_3_2())!=0:
            list1[6]=1
        if len(mg1.gen_type_8_serial_single())!=0:
            list1[7]=1
        if len(mg1.gen_type_9_serial_pair())!=0 :
            list1[8]=1
        if len(mg1.gen_type_10_serial_triple())!=0 :
            list1[9]=1
        if len(mg1.gen_type_12_serial_3_2())!=0 :
            list1[10]=1
        if len(mg1.gen_type_13_4_2())!=0 :
            list1[11]=1
        if len(mg1.gen_type_14_4_22())!=0:
            list1[12]=1
    return list1
# import time
def combine_all(n,b,a,up,down,lastplay):   #??????????????????????????????????????????????????????????????????????????????????????????????????????
    
    # time1 = time.time()
    list1to11,list109to119,list218to228=sort_single(n,a,b)
    list12to22,list120to130,list229to239=sort_double(n,a,b)
    list23to28,list131to136,list240to245=sort_triple(n,a,b)
    list29to34,list137to142,list246to251=sort_3plus1(n,a,b)
    list35to47,list143to155,list252to264=sort_serial_single(n,a,b)
    list48to60,list156to168,list265to277=sort_serial_pair(n,a,b)
    list61to72,list169to180,list278to289=sort_serial_triple(n,a,b)
    list73to81,list181to189,list290to298=sort_serial_triple_3_2(n,a,b)
    list82to85,list190to193,list299to302=sort_boom(n,a,b)
    list86to89,list194to197,list303to306=sort_4plus2(n,a,b)
    list90to91,list198to199,list307to308=sort_20_30(n,a,b)
    list92to102,list200to210,list309to319=leave_card_num(n,a,b)
    # time1end = time.time()-time1
    # print(time1end)
    
    # time2 = time.time()
    list103to108,list211to216,list320to325=min_shoushu1(n,a,b)
    list217,list326=brother(up,down)
    list327to340=sortgenpai1(lastplay)
    # time2end = time.time()-time2
    # print(time2end,'\n')
    
    return list1to11+list12to22+list23to28+list29to34+list35to47+list48to60+list61to72+list73to81+list82to85+list86to89+list90to91+list92to102+list103to108+list109to119+list120to130+list131to136+list137to142+list143to155+list156to168+list169to180+list181to189+list190to193+list194to197+list198to199+list200to210+list211to216+list217+list218to228+list229to239+list240to245+list246to251+list252to264+list265to277+list278to289+list290to298+list299to302+list303to306+list307to308+list309to319+list320to325+list326+list327to340




        





        


    


