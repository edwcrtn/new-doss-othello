import random
dico={'request': 'play', 'lives': 3, 'errors': [], 'state': {'players': ['Co', 'RECURSIVINATOR'], 'current': 1, 'board': [[3, 12, 42, 1, 10, 11, 19, 37, 23, 44, 36, 43, 5, 13, 21, 34, 35, 39, 31, 30, 24, 26, 27, 25, 28, 17, 29], [20, 0, 9, 18]]}}
lw=dico['state']['board'][1]   #liste black
lb=dico['state']['board'][0]   #liste white

bord=[0,1,2,3,4,5,6,7,15,23,31,39,47,55,63,62,61,60,59,58,57,56,48,40,32,24,16,8]
bordg=[0,8,16,24,32,40,48,56]  #bord droit
bordd=[7,15,23,31,39,47,55,63]  #bord gauche



def recursifb(lb,lw,cp,i,j,a,b):                #cp = coup possible 
    if i+j*(a-2) in bordd and j in [-7,+1,+9]:
        return None
    if i+j*(a-2) in bordg and j in [-9,-1,+7]:
        return None   
    if i+j*b in lw and i+j*a not in cp and i+j*a not in lb and i+j*a not in lw :
        if i+j*b in bordd and j in [-7,+1,+9]:
            return None
        if i+j*b in bordg and j in [-9,-1,+7]:
            return None  
        return i+j*a
    if i+j*b in lw and i+j*a not in cp and i+j*a not in lb and i+j*a in lw:
        a=a+1
        b+=1
        return(recursifb(lb,lw,cp,i,j,a,b))


def cpb(lbl,lwh):
    cpo=[]
    for i in lbl:
        for j in (-9,-8,-7,-1,+1,+7,+8,+9):
            if recursifb(lbl,lwh,cpo,i,j,2,1) != None:
                v=recursifb(lbl,lwh,cpo,i,j,2,1)
                if v in range(64):
                    cpo.append(v)
    return cpo

def recursifw(lb,lw,cp,i,j,a,b):
    if i+j*(a-2) in bordd and j in [-7,+1,+9]:
        return None
    if i+j*(a-2) in bordg and j in [-9,-1,+7]:
        return None    
    if i+j*b in lb and i+j*a not in cp and i+j*a not in lw and i+j*a not in lb:
        if i+j*b in bordd and j in [-7,+1,+9]:
            return None
        if i+j*b in bordg and j in [-9,-1,+7]:
            return None
        return i+j*a
    if i+j*b in lb and i+j*a not in cp and i+j*a not in lw and i+j*a in lb:
        a=a+1
        b+=1
        return(recursifw(lb,lw,cp,i,j,a,b))
    

def cpw(lbl,lwh):
    cpo=[]
    for i in lwh:
        for j in (-9,-8,-7,-1,+1,+7,+8,+9):
            if recursifw(lbl,lwh,cpo,i,j,2,1) != None:
                v=recursifw(lbl,lwh,cpo,i,j,2,1)
                if v in range(64):
                    cpo.append(v)
    return cpo


print(cpb(lb,lw))
print(cpw(lb,lw))