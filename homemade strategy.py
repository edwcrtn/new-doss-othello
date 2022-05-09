import random

dico={'request': 'play', 'lives': 3, 'errors': [], 'state': {'players': ['Edwin et Tim1', 'Edwin et Tim2'], 'current': 1, 'board': [[0], [1,2,8]]}}
lw=dico['state']['board'][1]
lb=dico['state']['board'][0]

bord=[0,1,2,3,4,5,6,7,15,23,31,39,47,55,63,62,61,60,59,58,57,56,48,40,32,24,16,8]
bordg=[0,8,16,24,32,40,48,56]
bordd=[7,15,23,31,39,47,55,63]


def recursifb(lb,lw,cp,i,j,a,b):
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

corners=[0,7,53,56]

def pionsprisb(lw,lb,coup,j,a=2,b=1):
    case = coup 
    if case+j*a not in range(64):
        return None
    if case+j*a not in lw and case+j*a not in lb:
        return None
    if case+j*a in lb:
        return b
    else:
        a+=1
        b+=1
        return(pionsprisb(lw,lb,coup,j,a,b))

def bestb():                                                    #renvoie le coup qui prend le plus de pion d'un coup
    max={"coup":None,"points":0}
    for coup in cpb(lb,lw):
        for j in (-9,-8,-7,-1,+1,+7,+8,+9):
            if pionsprisb(lw,lb,coup,j) !=None:
                if pionsprisb(lw,lb,coup,j)>max["points"]:
                    max["coup"]=coup
                    max["points"]=pionsprisb(lw,lb,coup,j)
    return max["coup"]


def pionsprisw(lw,lb,coup,j,a=2,b=1):
    case = coup 
    if case+j*a not in range(64):
        return None
    if case+j*a not in lw and case+j*a not in lb:
        return None
    if case+j*a in lw:
        return b
    else:
        a+=1
        b+=1
        return(pionsprisw(lw,lb,coup,j,a,b))

def bestw():                                                    #renvoie le coup qui prend le plus de pion d'un coup
    max={"coup":None,"points":0}
    for coup in cpw(lb,lw):
        for j in (-9,-8,-7,-1,+1,+7,+8,+9):
            if pionsprisw(lw,lb,coup,j) !=None:
                if pionsprisw(lw,lb,coup,j)>max["points"]:
                    max["coup"]=coup
                    max["points"]=pionsprisw(lw,lb,coup,j)
    return max["coup"]


print(bestb())
print(bestw())

