#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 13:34:22 2017

@author: hila yanay brot

hillay@gmail.com
"""

import sys
sys.path.append("/home/hilla/EdgesRemoval/code")
import Add_Remove as ar

N=10000
conn=0.005
iter_num=1000000
coeff=2

Edges,net_edges,net_loc,prob_list=\
ar.InitiatRandomNetwork(N,conn)
for t in range(iter_num):
    Edges,net_edges,net_loc,prob_list,loc=\
    ar.DeleteRandomEdges(Edges,net_edges,net_loc,prob_list)
    Edges,net_edges,net_loc,prob_list=\
    ar.TriadicClosor(Edges,net_edges,net_loc,prob_list,loc,N)
Edges1=Edges
print('1')

Edges,net_edges,net_loc,prob_list=\
ar.InitiatRandomNetwork(N,conn)    
for t in range(iter_num):
    Edges,net_edges,net_loc,prob_list,loc=\
    ar.DeleteRandomEdgesNode(Edges,net_edges,net_loc,prob_list,N)
    Edges,net_edges,net_loc,prob_list=\
    ar.TriadicClosor(Edges,net_edges,net_loc,prob_list,loc,N)
Edges2=Edges
print('2')

Edges,net_edges,net_loc,prob_list=\
ar.InitiatRandomNetwork(N,conn)    
for t in range(iter_num):
    Edges,net_edges,net_loc,prob_list,loc=\
    ar.DeleteRandomEdges(Edges,net_edges,net_loc,prob_list)
    Edges,net_edges,net_loc,prob_list=\
    ar.PALinear(Edges,net_edges,net_loc,prob_list,loc,N)
Edges3=Edges
print('3')

Edges,net_edges,net_loc,prob_list=\
ar.InitiatRandomNetwork(N,conn)    
for t in range(iter_num):
    Edges,net_edges,net_loc,prob_list,loc=\
    ar.DeleteRandomEdgesNode(Edges,net_edges,net_loc,prob_list,N)
    Edges,net_edges,net_loc,prob_list=\
    ar.PALinear(Edges,net_edges,net_loc,prob_list,loc,N)    
Edges4=Edges
print('4')

iter_num=500000
Edges,net_edges,net_loc,prob_list=\
ar.InitiatRandomNetwork(N,conn)
for t in range(iter_num):
    Edges,net_edges,net_loc,prob_list,loc=\
    ar.DeleteRandomEdgesNode(Edges,net_edges,net_loc,prob_list,N)
    Edges,net_edges,net_loc,prob_list=\
    ar.PAEnhanced(Edges,net_edges,net_loc,prob_list,loc,N,2) 
Edges5=Edges
print('5')

Edges,net_edges,net_loc,prob_list=\
ar.InitiatRandomNetwork(N,conn)    
for t in range(iter_num):
    Edges,net_edges,net_loc,prob_list,loc=\
    ar.DeleteRandomEdges(Edges,net_edges,net_loc,prob_list)
    Edges,net_edges,net_loc,prob_list=\
    ar.PAEnhanced(Edges,net_edges,net_loc,prob_list,loc,N,2)
Edges6=Edges
print('6')