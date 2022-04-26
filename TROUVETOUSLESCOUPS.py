import random
dico={'request': 'play', 'lives': 3, 'errors': [], 'state': {'players': ['Edwin et Tim2', 'Edwin et Tim1'], 'current': 1, 'board': [[23, 30, 26, 28, 34, 35, 44, 37, 36], [14, 21, 42, 19, 20, 27, 45, 29]]}}
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
                v=recursifb(lbl,lwh,cpo,i,j,2)
                if v>0 and v<64:
                    cpo.append(v)
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
                v=recursifw(lbl,lwh,cpo,i,j,2)
                if v>0 and v<64:
                    cpo.append(v)
    return cpo

print(cpw(lb,lw))


