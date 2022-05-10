import DERNIERE_VERSION

dico={'request': 'play', 'lives': 3, 'errors': [], 'state': {'players': ['Edwin et Tim1', 'Edwin et Tim2'], 'current': 0, 'board': [[58, 50, 4, 11, 13, 20, 22, 29, 25, 48, 49, 21, 28, 37, 51, 36, 35, 16, 24, 40, 32, 55], [2, 10, 18, 63, 27, 45, 54, 60, 52, 8, 26, 17, 41, 34, 44, 42, 43, 23]]}}
lw=dico['state']['board'][1]
lb=dico['state']['board'][0]

bord=[0,1,2,3,4,5,6,7,15,23,31,39,47,55,63,62,61,60,59,58,57,56,48,40,32,24,16,8]
bordg=[0,8,16,24,32,40,48,56]
bordd=[7,15,23,31,39,47,55,63]

def test_cpb():
    assert DERNIERE_VERSION.cpb(lb,lw)==[9, 61, 33, 53, 19, 0, 3, 46]
    assert DERNIERE_VERSION.cpw(lb,lw)==[38, 12, 47, 6, 30, 5, 56, 33, 57, 59, 14, 15, 19]
    assert DERNIERE_VERSION.bestb(lb,lw)==46
    assert DERNIERE_VERSION.bestw(lb,lw)==56