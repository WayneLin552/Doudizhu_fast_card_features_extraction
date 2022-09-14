# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 21:33:36 2022

@author: LinMouwei
"""

import random
import time
import numpy as np
import get_eig_lmw as lmw
from fun340 import features340, get_min_shoushu, get_min_shoushu_old, features340_old
import matplotlib.pyplot as plt
#from min_playtimes import gen_min_playtimes




#3-k分别是3-13，A是14,2是17，小王是20，大王是30
card_dic=[3]*4+[4]*4+[5]*4+[6]*4+[7]*4+[8]*4+[9]*4+[10]*4+[11]*4+[12]*4+[13]*4+[14]*4+[17]*4+[20]+[30]


handcards_own = []
handcards_up = []
handcards_down = []
handcards=[]
time_lmw=[]
time_newdfs=[]
time_olddfs=[]
playtime_lmw=[]
playtime_newdfs=[]
playtime_olddfs=[]

for i in range(20000):
    handcards.append(random.sample(card_dic, 17))


for card in handcards:

    temptime = time.time()
    newcard = lmw.card_trans(card)
    result = lmw.get_min_playhands(newcard)
    temptime_end=time.time()-temptime
    time_lmw.append(temptime_end)
    playtime_lmw.append(result)


    temptime = time.time()
    playtimes = get_min_shoushu(card)
    temptime_end=time.time()-temptime
    time_newdfs.append(temptime_end)
    playtime_newdfs.append(playtimes)    
    
    temptime = time.time()
    playtimes = get_min_shoushu_old(card)
    temptime_end=time.time()-temptime
    time_olddfs.append(temptime_end)
    playtime_olddfs.append(playtimes)  
    

plt.plot(range(20000),sorted(time_lmw),label='new_with_bimatrix')
plt.plot(range(20000),sorted(time_newdfs),label='new_without_bimatrix')  
plt.plot(range(20000),sorted(time_olddfs),label='old')    
plt.legend(['new_with_bimatrix','new_without_bimatrix','old'])
plt.xlabel('sorted: 20000 random dealt')
plt.ylabel('time: s')
plt.title('Time consumption for minimum playhands')
# print('sum_sub:',np.sum(playtime_lmw)-np.sum(playtime_old))
# plt.ylim(0.1,0.7)
# plt.xlim(18000,20100)
print('avg_new_with_bimatrix:',np.mean(time_lmw),'\nnew_without_bimatrix:',np.mean(time_newdfs),'\nold:',np.mean(time_olddfs))




# time_lmw_all=[]
# time_newdfs_all=[]
# time_olddfs_all=[]
# for i in range(20000):
#     random.shuffle(card_dic)
#     handcards_own.append(card_dic[:17])
#     handcards_up.append(card_dic[17:34])
#     handcards_down.append(card_dic[34:])
    
# for own, up, down in zip(handcards_own,handcards_up,handcards_down):
    
#     time1 = time.time()
#     results_lmw = lmw.combine_all(own,up,down,0,1,[])
#     time1end = time.time()-time1    
#     time_lmw_all.append(time1end)
    
#     temptime = time.time()
#     results_newdfs = features340(own,up,down,0,1,[])
#     timeend = time.time()-temptime
#     time_newdfs_all.append(timeend)
    
#     temptime = time.time()
#     results_olddfs = features340_old(own,up,down,0,1,[])
#     timeend = time.time()-temptime
#     time_olddfs_all.append(timeend)    
    
# plt.plot(range(20000),sorted(time_lmw_all),label='new_with_bimatrix')
# plt.plot(range(20000),sorted(time_newdfs_all),label='new_without_bimatrix')  
# plt.plot(range(20000),sorted(time_olddfs_all),label='old')    
# plt.legend(['new_with_bimatrix','new_without_bimatrix','old'])
# plt.xlabel('sorted: 20000 random dealt')
# plt.ylabel('time: s')
# plt.title('Time consumption for all features')
# # print('sum_sub:',np.sum(playtime_lmw)-np.sum(playtime_old))
# # plt.ylim(0.1,0.7)
# # plt.xlim(18000,20100)
# print('avg_new_with_bimatrix:',np.mean(time_lmw_all),'\nnew_without_bimatrix:',np.mean(time_newdfs_all),'\nold:',np.mean(time_olddfs_all))