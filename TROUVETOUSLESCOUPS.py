import random
dico={'request': 'play', 'lives': 3, 'errors': [], 'state': {'players': ['Edwin et Tim2', 'Edwin et Tim1'], 'current': 0, 'board': [[40, 58, 50, 52, 51, 43, 7, 14, 8, 48, 49, 3, 19, 27, 35], [20, 38, 37, 36, 53, 44, 45, 59, 17, 26, 18, 31, 28, 30, 29, 56, 42, 6, 22, 13, 21, 33, 34, 41, 25, 0, 9, 2, 1, 11, 10]]}}
#dico={'request': 'play', 'lives': 3, 'errors': [], 'state': {'players': ['Edwin et Tim2', 'Edwin et Tim1'], 'current': 1, 'board': [[23, 30, 26, 28, 34, 35, 44, 37, 36], [14, 21, 42, 19, 20, 27, 45, 29]]}}
lb=dico['state']['board'][0]
lw=dico['state']['board'][1]
print(dico['lives'])

bord=[0,1,2,3,4,5,6,7,15,23,31,39,47,55,63,62,61,60,59,58,57,56,48,40,32,24,16,8]

def recursifb(lb,lw,cp,i,j,a):
    #if a>1:
    #    if i+j in lw and i+j*(a) in lb and i+j*a+1 in bord:
    #        return None
    if i+j*(a-1)not in bord:
        if i+j in lw and i+j*a not in cp and i+j*a not in lb and i+j*a not in lw:
            return i+j*a
    if i+j in lw and i+j*a not in cp and i+j*a not in lb and i+j*a in lw:
        a=a+1
        return(recursifb(lb,lw,cp,i,j,a))


def cpob(lbl,lwh):
    cpo=[]
    for i in lbl:
        for j in (-9,-8,-7,-1,+1,+7,+8,+9):
            if recursifb(lbl,lwh,cpo,i,j,2) != None:
                v=recursifb(lbl,lwh,cpo,i,j,2)
                cpo.append(v)
    return cpo


def recursifw(lb,lw,cp,i,j,a):
    if i+j*(a-1)not in bord:
        if i+j in lb and i+j*a not in cp and i+j*a not in lw and i+j*a not in lb:
            return i+j*a
    if i+j in lb and i+j*a not in cp and i+j*a not in lw and i+j*a in lb:
        a=a+1
        return(recursifw(lb,lw,cp,i,j,a))
    

def cpow(lbl,lwh):
    cpo=[]
    for i in lwh:
        for j in (-9,-8,-7,-1,+1,+7,+8,+9):
            if recursifw(lbl,lwh,cpo,i,j,2) != None:
                v=recursifw(lbl,lwh,cpo,i,j,2)
                cpo.append(v)
    return cpo


print("Coups possibles pour les noirs : ")
print(cpob(lb,lw))

print("Coups possibles pour les blancs : ")
print(cpow(lb,lw))

case=random.choice(cpow(lb,lw))


