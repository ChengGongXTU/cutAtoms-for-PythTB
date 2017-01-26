from pythtb import *
import numpy as np

def turnlist(orbarr):     # turn a array to be a list
    orblist = []
    if len(np.shape(orbarr)) == 1:
        m = np.shape(orbarr)[0]
        for i in range(m):
            orblist.append(orbarr[i])
    elif len(np.shape(orbarr)) == 2:       
        m,n = np.shape(orbarr)
        for i in range(m):
            one_orb = []
            for j in range(n):
                one_orb.append(orbarr[i][j])
            orblist.append(one_orb)
    return orblist
    
def resetlist(del_list):   # a special algorithm sorts list to oder numbers fromsmallest to largest, 
    new_list = []          # and change the numbers' value.
    del_number = 0
    for i in range(len(del_list)):
        new_list.append(del_list[i]-del_number)
        del_number = del_number + 1
    return new_list
    
def delatoms(del_list,slab_orb):    # del atoms
    for i in del_list:
        del slab_orb[i]
    return slab_orb
    
def resethoppings(i,slab_hoppings):  #del the hoppings of specific atoms
    i_num = 0
    for f in range(len(slab_hoppings)):
        if slab_hoppings[f][1] == i:
            i_num = i_num + 1            
        elif slab_hoppings[f][2] == i:
            i_num = i_num + 1
    for h in range(i_num):
        for j in range(len(slab_hoppings)): # change atoms'number -1.
            if slab_hoppings[j][1] == i:    # if atoms'number >i, del No.i atoms'hop.
                del slab_hoppings[j]
                break
            elif slab_hoppings[j][2] == i:
                del slab_hoppings[j]
                break
    for k in range(len(slab_hoppings)):
        if slab_hoppings[k][1] > i:
            slab_hoppings[k][1] = slab_hoppings[k][1] - 1
        if slab_hoppings[k][2] > i:
            slab_hoppings[k][2] = slab_hoppings[k][2] - 1
    return slab_hoppings

def cutAtoms(del_list,slab_model):  # input atoms' number and TBmodel's name
    slab_norb = slab_model._norb    
    slab_orb = turnlist(slab_model._orb)
    slab_hoppings = slab_model._hoppings
    slab_onsite = turnlist(slab_model._site_energies)
#    del_list = [0,199]
    new_del_list = resetlist(del_list)
    
    #  del some atoms in del_list
    slab_model._orb = np.array(delatoms(new_del_list,slab_orb))
    slab_model._norb = slab_norb - len(new_del_list)
    slab_model._nsta = slab_model._norb*slab_model._nspin
    
    #del onsite-energy in del_list
    slab_model._site_energies = np.array(delatoms(new_del_list,slab_onsite))
    
    #del hoppings in del_list
    for i in new_del_list:
        resethoppings(i,slab_hoppings)
        
    slab_model._hoppings = slab_hoppings
    

