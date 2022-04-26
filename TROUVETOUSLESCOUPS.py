dico={'request': 'play', 'lives': 2, 'errors': [{'message': 'Edwin et Tim2 take too long to respond: 17.311607837677002s', 'state': {'players': ['Edwin et Tim2', 'Edwin et Tim1'], 'current': 1, 'board': [[28, 35, 26, 27], [36]]}, 'move': 26}], 'state': {'players': ['Edwin et Tim2', 'Edwin et Tim1'], 'current': 0, 'board': [[35, 26, 27], [29,30,36, 20, 28]]}}
#print(dico)
lb=dico['state']['board'][0]
lw=dico['state']['board'][1]

#j'ai rendu ça récursif
#ne marche que pour les NWARS 
#NE PRENDS PAS EN COMPTE LES BORDS !!!!

def recursifb(lb,lw,cp,i,j,a):
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


