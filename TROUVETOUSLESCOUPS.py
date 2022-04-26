import random
dico={'request': 'play', 'lives': 3, 'errors': [], 'state': {'players': ['Edwin et Tim2', 'Edwin et Tim1'], 'current': 0, 'board': [[22, 29, 4, 13, 48, 41, 20, 32, 34, 33], [28, 45, 36, 25, 26, 44, 5, 19, 12, 59, 51, 27, 35, 43]]}}
#print(dico)
lb=dico['state']['board'][0]
lw=dico['state']['board'][1]
print(dico['lives'])

#j'ai rendu ça récursif
#ne marche que pour les NWARS 
#NE PRENDS PAS EN COMPTE LES BORDS !!!!

def recursifb(lb,lw,cp,i,j,a):
    if i+j in lb and i+j*a in lw and i+j*a in bord:
        return None

    if i+j in lw and i+j*a not in cp and i+j*a not in lb and i+j*a not in lw:
        return i+j*a
    if i+j in lw and i+j*a not in cp and i+j*a not in lb and i+j*a in lw:
        a=a+1
        return(recursifb(lb,lw,cp,i,j,a))


def cpb(lbl,lwh):
    cpo=[]
    for i in lbl:
        for j in (-9,-8,-7,-1,+1,+7,+8,+9):
            if recursifb(lbl,lwh,cpo,i,j,2) != None:
                cpo.append(recursifb(lbl,lwh,cpo,i,j,2))
    return cpo

print(cpb(lb,lw))

def recursifw(lb,lw,cp,i,j,a):
    if i+j in lb and i+j*a in lb and i+j*a in bord:
        return None
    
    if i+j in lb and i+j*a not in cp and i+j*a not in lw and i+j*a not in lb:
        return i+j*a
    if i+j in lb and i+j*a not in cp and i+j*a not in lw and i+j*a in lb:
        a=a+1
        return(recursifw(lb,lw,cp,i,j,a))
    

def cpw(lbl,lwh):
    cpo=[]
    for i in lwh:
        for j in (-9,-8,-7,-1,+1,+7,+8,+9):
            if recursifw(lbl,lwh,cpo,i,j,2) != None:
                cpo.append(recursifw(lbl,lwh,cpo,i,j,2))
    return cpo

print(cpw(lb,lw))


