import copy
#import pandas as pd
#import numpy as np
from collections import Counter
from move_generator import MovesGener
#from min_play_times import min_play_times
from decompose import decomposeMin,cardsFrom#,decomposeLoose, cardsFrom_old
from handcards_old import decomposeLoose

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

def sort_single(nn,aa,bb): #处理单张 当前手牌1-11 下家手牌12-22 上家手牌23-33
    list1=[0]*11
    list2=[0]*11
    list3=[0]*11
    n=list(set(nn))
    a=list(set(aa))
    b=list(set(bb))
    
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


def sort_double(n,a,b): #处理对子  当前玩家34-44 下家45-55 上家56-66
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
            if nnd!=[]:  #x不空 n空
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

def sort_triple(n,a,b): #处理三对 当前67-72 下家73-78 上家79-84 
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
            if nnd!=[]:  #x不空 n空
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

def sort_3plus1(n,a,b): #处理三带一 当前85-90 下家91-96 上家97-102
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
            if nnd!=[]:  #x不空 n空
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

# 顺子 当前五连顺、六连、七连 103-115 下家116-128 上家129-141
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
    list1=[0]*4 #1-9 当前567 下家567 上家567
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
            if n_list_5_1 != []:  # x不空 n空
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
            if n_list_7_1 != []:  # x不空 n空
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
            if n_list_6_1 != []:  # x不空 n空
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

#连对 当前三四五连对 142-154 下家三四五连对155-167 上家三四五连对168-180
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
            if n_list_3_1 != []:  # x不空 n不空
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
            if n_list_4_1 != []:  # x不空 n不空
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
            if n_list_5_1 != []:  # x不空 n不空
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

def sort_serial_triple(n,a,b): #当前二三四飞机 181-193 下家194-206 上家207-219
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
    
    for j in range(3): #三连飞机
        x = BiggerList(n_list_3_1, b_list_3_1)
        x = copy.copy(BiggerList(x, a_list_3_1))
        if x != []:
            if n_list_3_1 != []:  # x不空 n空
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
        
    for j in range(3): #四连飞机
        x = BiggerList(n_list_4_1, b_list_4_1)
        x = copy.copy(BiggerList(x, a_list_4_1))
        if x != []:
            if n_list_4_1 != []:  # x不空 n空
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
        
    for j in range(3): #二连飞机
        x = BiggerList(n_list_2_1, b_list_2_1)
        x = copy.copy(BiggerList(x, a_list_2_1))
        if x != []:
            if n_list_2_1 != []:  # x不空 n空
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

def sort_boom(n,a,b): #处理炸弹 当前玩家220-213 下家214-217 上家218-221
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
            if nnd!=[]:  #x不空 n空
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

def sort_4plus2(n,a,b): #处理四带二 当前 222-235 下家236-239 上家240-243
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
            if nnd!=[]:  #x不空 n空
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

def sort_20_30(n,a,b): #处理是否有王炸和大小王 当前玩家244-245 下家246-247 上家248-249
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

def leave_card_num(nn,aa,bb): #处理剩余几张牌 当前玩家 250-260 下家261-271 上家272-282
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

def brother(role,rolea): #rolea是下家的role #下家农民队友283 上家农民队友284
    list1=[0] #下家是否是队友
    list2=[0] #上家是否是队友
    if role==0:
        if rolea==0:
            list1[0]=1 #下家是农民队友
        else:
            list2[0]=1 #上家是农民队友
    return list1,list2

def sort_serial_triple_3_2(n,a,b): #当前玩家二连三连飞机带对子 285-293 下家294-302 上家303-311
    mgn = MovesGener(n)
    mgb = MovesGener(b)
    mga = MovesGener(a)
    n_triple_move = mgn.gen_type_12_serial_3_2()
    b_triple_move = mgb.gen_type_12_serial_3_2()
    a_triple_move = mga.gen_type_12_serial_3_2()
    n_list_2, n_list_3,  n_list_other = fenlei_3(n_triple_move)
    b_list_2, b_list_3,  b_list_other = fenlei_3(b_triple_move)
    a_list_2, a_list_3,  a_list_other = fenlei_3(a_triple_move)
    list1=[0]*4 #1-9 当前23 下家23 上家23
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
            if n_list_2_1 != []:  # x不空 n空
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
            if n_list_3_1 != []:  # x不空 n空
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

# def shoushu(result_dict):
#     a = list(result_dict.values())
#     return a[-1]

# def min_shoushu(n,a,b): #最小手数 当前玩家312-317 下家318-323 上家324-329
#     n_dict = min_play_times(n, {})
#     b_dict = min_play_times(b, {})
#     a_dict = min_play_times(a, {})
#     n_ss = shoushu(n_dict)
#     b_ss = shoushu(b_dict)
#     a_ss = shoushu(a_dict)
#     list1=[0]*6
#     list2=[0]*6
#     list3=[0]*6
    
#     if n_ss <= 5 and n_ss != 0:
#         list1[n_ss-1]=1
#     elif n_ss > 5:
#         list1[-1]=1
#     if b_ss <= 5 and b_ss != 0:
#         list3[b_ss-1]=1
#     elif b_ss > 5:
#         list3[-1]=1
#     if a_ss <= 5 and a_ss != 0:
#         list2[a_ss-1]=1
#     elif a_ss > 5:
#         list2[-1]=1
#     return list1,list2,list3

def get_min_shoushu(x):
    # replace_dict={'1':3, '2':4, '3':5, \
    #                 '4':6, '5':7, '6':8, '7':9, '8':10, '9':11, '10':12, '11':13, \
    #                 '12':14, '13':2, '14':0, '15':1}
    replace_dict = {17:2,20:0,30:1}
    r_x=[replace_dict[i] if i in replace_dict else i for i in x]
    a = Counter(r_x)
    try:
        b = cardsFrom(*a.items())
        return decomposeMin(b)
    except:
        print('报错的x_new',x)
        return 1

def get_min_shoushu_old(x):
    # replace_dict={'1':3, '2':4, '3':5, \
    #                 '4':6, '5':7, '6':8, '7':9, '8':10, '9':11, '10':12, '11':13, \
    #                 '12':14, '13':2, '14':0, '15':1}
    # replace_dict = {17:2,20:0,30:1}
    # r_x=[replace_dict[i] if i in replace_dict else i for i in x]
    # a = Counter(r_x)
    try:
        # b = cardsFrom_old(*a.items())
        result =  decomposeLoose(x)
        return result
    except:
        print('报错的x_old',x)
        return 1    



def min_shoushu1(n,a,b): #最小手数 当前玩家312-317 下家318-323 上家324-329
    n_ss = get_min_shoushu(n)
    b_ss = get_min_shoushu(b)
    a_ss = get_min_shoushu(a)
    list1=[0]*6
    list2=[0]*6
    list3=[0]*6
    
    if n_ss <= 5 and n_ss != 0:
        list1[n_ss-1]=1
    elif n_ss > 5:
        list1[-1]=1
    if b_ss <= 5 and b_ss != 0:
        list3[b_ss-1]=1
    elif b_ss > 5:
        list3[-1]=1
    if a_ss <= 5 and a_ss != 0:
        list2[a_ss-1]=1
    elif a_ss > 5:
        list2[-1]=1
    return list1,list2,list3

def min_shoushu1_old(n,a,b): #最小手数 当前玩家312-317 下家318-323 上家324-329
    n_ss = get_min_shoushu_old(n)
    b_ss = get_min_shoushu_old(b)
    a_ss = get_min_shoushu_old(a)
    list1=[0]*6
    list2=[0]*6
    list3=[0]*6
    
    if n_ss <= 5 and n_ss != 0:
        list1[n_ss-1]=1
    elif n_ss > 5:
        list1[-1]=1
    if b_ss <= 5 and b_ss != 0:
        list3[b_ss-1]=1
    elif b_ss > 5:
        list3[-1]=1
    if a_ss <= 5 and a_ss != 0:
        list2[a_ss-1]=1
    elif a_ss > 5:
        list2[-1]=1
    return list1,list2,list3


def sortgenpai1(x): #跟牌特征330-343
    list1=[0]*14     
    if x==[]:
        list1[-1]=1
    else:# x不空
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

def features340(n,b,a,role,rolea,lastplay):   #参数分别是当前手牌，上家手牌，下家手牌，当前角色，下家角色，上家出牌，上上家出牌
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
    list103to108,list211to216,list320to325=min_shoushu1(n,a,b)
    list217,list326=brother(role,rolea)
    list327to340=sortgenpai1(lastplay)
    return list1to11+list12to22+list23to28+list29to34+list35to47+list48to60+list61to72+list73to81+list82to85+list86to89+list90to91+list92to102+list103to108+list109to119+list120to130+list131to136+list137to142+list143to155+list156to168+list169to180+list181to189+list190to193+list194to197+list198to199+list200to210+list211to216+list217+list218to228+list229to239+list240to245+list246to251+list252to264+list265to277+list278to289+list290to298+list299to302+list303to306+list307to308+list309to319+list320to325+list326+list327to340


def features340_old(n,b,a,role,rolea,lastplay):   #参数分别是当前手牌，上家手牌，下家手牌，当前角色，下家角色，上家出牌，上上家出牌
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
    list103to108,list211to216,list320to325=min_shoushu1_old(n,a,b)
    list217,list326=brother(role,rolea)
    list327to340=sortgenpai1(lastplay)
    return list1to11+list12to22+list23to28+list29to34+list35to47+list48to60+list61to72+list73to81+list82to85+list86to89+list90to91+list92to102+list103to108+list109to119+list120to130+list131to136+list137to142+list143to155+list156to168+list169to180+list181to189+list190to193+list194to197+list198to199+list200to210+list211to216+list217+list218to228+list229to239+list240to245+list246to251+list252to264+list265to277+list278to289+list290to298+list299to302+list303to306+list307to308+list309to319+list320to325+list326+list327to340

        





        


    
