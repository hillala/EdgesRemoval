#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 13:24:33 2017

@author: hila yanay brot

hillay@gmail.com
"""
from __future__ import division, print_function
import numpy as np 
import random

def InitiatRandomNetwork(N,conn):
    Edges=np.random.randint(N, size=(2, int(np.floor(((N*(N-1)))*conn))))
    Edges=Edges[:,Edges[0,:]>Edges[1,:]]
    for k in range(N):
        Edges[0,:]==N
    Edges = UniqueRows(Edges)
    vec=np.arange(Edges.shape[1])
    net_edges=[None] * N
    net_loc=[None] * N
    prob_list=[]
    for k in range(N):
        net_edges[k]=list(np.concatenate((Edges[1,Edges[0,:]==k],Edges[0,Edges[1,:]==k]),axis=0))
        net_loc[k]=list(np.concatenate((vec[Edges[0,:]==k],vec[Edges[1,:]==k]),axis=0))
        prob_list.append(np.zeros(len(net_edges[k])+1)+k)
        
    prob_list=list(np.array(np.concatenate(prob_list , axis=0),dtype=int))
    return Edges,net_edges,net_loc,prob_list 

def DeleteRandomEdges(Edges,net_edges,net_loc,prob_list):
      loc=np.random.randint(Edges.shape[1],size=1)
      print(Edges.shape[1])
      print(loc)
      nodes=Edges[:,loc]
      net_edges[int(nodes[0])].remove(nodes[1])
      net_edges[int(nodes[1])].remove(nodes[0])
      net_loc[int(nodes[0])].remove(loc)
      net_loc[int(nodes[1])].remove(loc)
      prob_list.remove(nodes[0])
      prob_list.remove(nodes[1])
      return Edges,net_edges,net_loc,prob_list,loc

def DeleteRandomEdgesNode(Edges,net_edges,net_loc,prob_list,N):
      N1=np.random.randint(N,size=1)
      flag=0
      while flag==0:
          if len(net_edges[N1])>0:
              l1=np.random.randint(len(net_edges[N1]),size=1)
              N2=net_edges[N1][l1]
              loc=net_loc[N1][l1]
              net_edges[N1].remove(N2)
              net_edges[N2].remove(N1)
              net_loc[N1].remove(loc)
              net_loc[N2].remove(loc)
              prob_list.remove(N1)
              prob_list.remove(N2)
              flag=1
      else:
          N1=np.random.randint(N,size=1)
      return Edges,net_edges,net_loc,prob_list,loc

def DeleteRandomNode(Edges,net_edges,net_loc,prob_list,N):
      N1=np.random.randint(N,size=1)
      flag=0
      while flag==0:
          num=len(net_edges[N1])
          if len(net_edges[N1])>0:
              remove_loc=net_loc[N1]
              remove_nodes=net_edges[N1]
              net_loc[N1]=[]
              net_edges[N1]=[]
              for k in range(num):
                  net_edges[remove_nodes[k]].remove(N1)
                  net_loc[remove_nodes[k]].remove(remove_loc[k])
                  prob_list.remove(N1)
                  prob_list.remove(remove_nodes[k])
                  flag=1
          else:
              N1=np.random.randint(N,size=1)
      return Edges,net_edges,net_loc,prob_list,remove_loc

  
def PALinear(Edges,net_edges,net_loc,prob_list,loc,N):
    N1=prob_list[int(np.random.randint(len(prob_list), size=(1)))]
    N2=int(np.random.randint(N, size=(1)))
    flag=0
    while flag==0:
        if N2 not in net_edges[N1]:
            net_edges[N1].append(N2)
            net_edges[N2].append(N1)
            net_loc[N1].append(loc)
            net_loc[N2].append(loc)
            Edges[0,loc]=N1
            Edges[1,loc]=N2
            prob_list.append(N1)
            prob_list.append(N2)
            flag=1
        else:
            N1=prob_list[int(np.random.randint(len(prob_list), size=(1)))]
            N2=int(np.random.randint(N, size=(1)))
    return Edges,net_edges,net_loc,prob_list 

def PAEnhanced(Edges,net_edges,net_loc,prob_list,loc,N,coeff):
    prob_list2=np.repeat(prob_list, coeff)
    N1=int(prob_list2[np.random.randint(len(prob_list2), size=(1))])
    N2=int(np.random.randint(N, size=(1)))
    flag=0
    while flag==0:
        if N2 not in net_edges[N1]:
            net_edges[N1].append(N2)
            net_edges[N2].append(N1)
            net_loc[N1].append(loc)
            net_loc[N2].append(loc)
            Edges[0,loc]=N1
            Edges[1,loc]=N2
            prob_list.append(N1)
            prob_list.append(N2)
            flag=1
        else:
            N1=int(prob_list2[np.random.randint(len(prob_list2), size=(1))])
            N2=int(np.random.randint(N, size=(1)))
    return Edges,net_edges,net_loc,prob_list 

def TriadicClosor(Edges,net_edges,net_loc,prob_list,loc,N):
    N1=prob_list[int(np.random.randint(N, size=(1)))]
    num=len(net_edges[N1])
    flag=0
    while flag==0:
        if num>1:
            l1=random.sample(np.arange(num), 2)
            nodes=[net_edges[N1][i] for i in l1]
            if nodes[1] not in net_edges[nodes[0]]: 
                Edges[0,loc]=nodes[0]
                Edges[1,loc]=nodes[1]
                net_edges[nodes[0]].append(nodes[1])
                net_edges[nodes[1]].append(nodes[0])
                net_loc[nodes[0]].append(loc)
                net_loc[nodes[1]].append(loc)
                prob_list.append(nodes[0])
                prob_list.append(nodes[1])
                flag=1
        else:
            N1=prob_list[int(np.random.randint(N, size=(1)))]
            num=len(net_edges[N1])
    return Edges,net_edges,net_loc,prob_list 
        
    
#def UniqueRows(x):    
#    y = np.ascontiguousarray(x).view(np.dtype((np.void, x.dtype.itemsize * x.shape[1])))
#    _, idx = np.unique(y, return_index=True)
#    return x[idx]