import DERNIERE_VERSION

dico={'request': 'play', 'lives': 3, 'errors': [], 'state': {'players': ['Edwin et Tim1', 'Edwin et Tim2'], 'current': 0, 'board': [[58, 50, 4, 11, 13, 20, 22, 29, 25, 48, 49, 21, 28, 37, 51, 36, 35, 16, 24, 40, 32, 55], [2, 10, 18, 63, 27, 45, 54, 60, 52, 8, 26, 17, 41, 34, 44, 42, 43, 23]]}}
lw=dico['state']['board'][1]
lb=dico['state']['board'][0]
dico2={'request': 'play', 'lives': 3, 'errors': [], 'state': {'players': ['Edwin et Tim1', 'Edwin et Tim2'], 'current': 0, 'board': [[2,6], [1,5]]}}
lw2=dico2['state']['board'][1]
lb2=dico2['state']['board'][0]
dico3={'request': 'play', 'lives': 3, 'errors': [], 'state': {'players': ['Edwin et Tim1', 'Edwin et Tim2'], 'current': 0, 'board': [[4], [3]]}}
lw3=dico3['state']['board'][1]
lb3=dico3['state']['board'][0]
dico4={'request': 'play', 'lives': 3, 'errors': [], 'state': {'players': ['Edwin et Tim1', 'Edwin et Tim2'], 'current': 0, 'board': [[11], [18]]}}
lw4=dico4['state']['board'][1]
lb4=dico4['state']['board'][0]
dico5={'request': 'play', 'lives': 3, 'errors': [], 'state': {'players': ['Edwin et Tim1', 'Edwin et Tim2'], 'current': 0, 'board': [[6], [5]]}}
lw5=dico5['state']['board'][1]
lb5=dico5['state']['board'][0]
dico6={'request': 'play', 'lives': 3, 'errors': [], 'state': {'players': ['Edwin et Tim1', 'Edwin et Tim2'], 'current': 0, 'board': [[28,35], [27,36]]}}
lw6=dico6['state']['board'][1]
lb6=dico6['state']['board'][0]
dico7={'request': 'play', 'lives': 3, 'errors': [], 'state': {'players': ['Edwin et Tim1', 'Edwin et Tim2'], 'current': 0, 'board': [[10], [19,28,37,46]]}}
lw7=dico7['state']['board'][1]
lb7=dico7['state']['board'][0]
dico8={'request': 'play', 'lives': 3, 'errors': [], 'state': {'players': ['Edwin et Tim1', 'Edwin et Tim2'], 'current': 0, 'board': [[18], [27]]}}
lw8=dico8['state']['board'][1]
lb8=dico8['state']['board'][0]

bord=[0,1,2,3,4,5,6,7,15,23,31,39,47,55,63,62,61,60,59,58,57,56,48,40,32,24,16,8]
bordg=[0,8,16,24,32,40,48,56]
bordd=[7,15,23,31,39,47,55,63]

tour1 =22
tour2 =4

def test_cpb():
    assert DERNIERE_VERSION.cpb(lb,lw)==[9, 61, 33, 53, 19, 0, 3, 46]
    assert DERNIERE_VERSION.cpw(lb,lw)==[38, 12, 47, 6, 30, 5, 56, 33, 57, 59, 14, 15, 19]
    assert DERNIERE_VERSION.bestb(lb,lw,tour1)==0
    assert DERNIERE_VERSION.bestw(lb,lw,tour1)==56
    assert DERNIERE_VERSION.bestb(lb,lw,tour2)==9
    assert DERNIERE_VERSION.bestw(lb,lw,tour2)==38
    assert DERNIERE_VERSION.bestb(lb2,lw2,tour2)==0
    assert DERNIERE_VERSION.bestw(lb2,lw2,tour2)==3
    assert DERNIERE_VERSION.bestb(lb3,lw3,tour2)==2
    assert DERNIERE_VERSION.bestw(lb3,lw3,tour2)==5
    assert DERNIERE_VERSION.bestb(lb4,lw4,tour2)==25
    assert DERNIERE_VERSION.bestw(lb4,lw4,tour2)==4
    assert DERNIERE_VERSION.bestb(lb4,lw4,tour1)==25
    assert DERNIERE_VERSION.bestw(lb4,lw4,tour1)==4
    assert DERNIERE_VERSION.bestb(lb5,lw5,tour2)==4
    assert DERNIERE_VERSION.bestw(lb5,lw5,tour2)==7
    assert DERNIERE_VERSION.bestb(lb6,lw6,tour2)==26
    assert DERNIERE_VERSION.bestw(lb6,lw6,tour2)==29
    assert DERNIERE_VERSION.bestb(lb7,lw7,tour2)==55
    assert DERNIERE_VERSION.bestw(lb7,lw7,tour2)==1
    assert DERNIERE_VERSION.bestw(lb8,lw8,tour2)==9