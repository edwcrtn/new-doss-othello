dico={'request': 'play', 'lives': 2, 'errors': [{'message': 'Edwin et Tim2 take too long to respond: 17.311607837677002s', 'state': {'players': ['Edwin et Tim2', 'Edwin et Tim1'], 'current': 1, 'board': [[28, 35, 26, 27], [36]]}, 'move': 26}], 'state': {'players': ['Edwin et Tim2', 'Edwin et Tim1'], 'current': 0, 'board': [[35, 26, 27], [29,30,36, 20, 28]]}}
#print(dico)
lb=dico['state']['board'][0]
lw=dico['state']['board'][1]



#ne sert plus
def coup(liste_black,liste_white):
    coups_possible=[]
    for i in liste_black:    #recu(i,-9,lb,lw) recu(i-8) recu(i-7) ...
        if i-9 in liste_white and i-9*2 not in coups_possible and i-9*2 not in liste_black and i-9*2 not in liste_white:
            coups_possible.append(i-9*2)
        if i-9 in liste_white and i-9*3 not in coups_possible and i-9*2 not in liste_black and i-9*2 in liste_white:
            coups_possible.append(i-9*3) #
        if i-8 in liste_white and i-8*2 not in coups_possible and i-8*2 not in liste_black and i-8*2 not in liste_white:
            coups_possible.append(i-8*2)
        if i-8 in liste_white and i-8*3 not in coups_possible and i-8*2 not in liste_black and i-8*2 in liste_white:
            coups_possible.append(i-8*3) #
        if i-7 in liste_white and i-7*2 not in coups_possible and i-7*2 not in liste_black and i-7*2 not in liste_white:
            coups_possible.append(i-7*2)
        if i-7 in liste_white and i-7*3 not in coups_possible and i-7*2 not in liste_black and i-7*2 in liste_white:
            coups_possible.append(i-7*3) #
        if i-1 in liste_white and i-1*2 not in coups_possible and i-1*2 not in liste_black and i-1*2 not in liste_white:
            coups_possible.append(i-1*2)
        if i-1 in liste_white and i-1*3 not in coups_possible and i-1*2 not in liste_black and i-1*2 in liste_white:
            coups_possible.append(i-1*3) #
        if i+1 in liste_white and i+1*2 not in coups_possible and i+1*2 not in liste_black and i+1*2 not in liste_white:
            coups_possible.append(i+1*2)
        if i+1 in liste_white and i+1*3 not in coups_possible and i+1*2 not in liste_black and i+1*2 in liste_white:
            coups_possible.append(i+1*3) #
        if i+7 in liste_white and i+7*2 not in coups_possible and i+7*2 not in liste_black and i+7*2 not in liste_white:
            coups_possible.append(i+7*2)
        if i+7 in liste_white and i+7*3 not in coups_possible and i+7*2 not in liste_black and i+7*2 in liste_white:
            coups_possible.append(i+7*3) #
        if i+8 in liste_white and i+8*2 not in coups_possible and i+8*2 not in liste_black and i+8*2 not in liste_white:
            coups_possible.append(i+8*2)
        if i+8 in liste_white and i+8*3 not in coups_possible and i+8*2 not in liste_black and i+8*2 in liste_white:
            coups_possible.append(i+8*3) #
        if i+9 in liste_white and i+9*2 not in coups_possible and i+9*2 not in liste_black and i+9*2 not in liste_white:
            coups_possible.append(i+9*2)
        if i+9 in liste_white and i+9*3 not in coups_possible and i+9*2 not in liste_black and i+9*2 in liste_white:
            coups_possible.append(i+9*3) #
    return coups_possible

#il faut rendre ça récursif !


print(coup(lb,lw))

#j'ai rendu ça récursif
#ne marche que pour les NWARS 
#NE PRENDS PAS EN COMPTE LES BORDS !!!!

def recursifb(lb,lw,cp,i,j,a):
    if i+j in lw and i+j*a not in cp and i+j*a not in lb and i+j*a not in lw:
        return i+j*a
    if i+j in lw and i+j*a not in cp and i+j*a not in lb and i+j*a in lw:
        a=a+1
        return(recursifb(lb,lw,cp,i,j,a))


def deux(lbl,lwh):
    cpo=[]
    for i in lbl:
        for j in (-9,-8,-7,-1,+1,+7,+8,+9):
            if recursifb(lbl,lwh,cpo,i,j,2) != None:
                cpo.append(recursifb(lbl,lwh,cpo,i,j,2))
    return cpo

print(deux(lb,lw))

def recursifw(lb,lw,cp,i,j,a):
    if i+j in lb and i+j*a not in cp and i+j*a not in lw and i+j*a not in lb:
        return i+j*a
    if i+j in lb and i+j*a not in cp and i+j*a not in lw and i+j*a in lb:
        a=a+1
        return(recursifw(lb,lw,cp,i,j,a))

def trois(lbl,lwh):
    cpo=[]
    for i in lwh:
        for j in (-9,-8,-7,-1,+1,+7,+8,+9):
            if recursifw(lbl,lwh,cpo,i,j,2) != None:
                cpo.append(recursifw(lbl,lwh,cpo,i,j,2))
    return cpo

print(trois(lb,lw))


