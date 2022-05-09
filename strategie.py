dico={'request': 'play', 'lives': 3, 'errors': [], 'state': {'players': ['Edwin et Tim2', 'Edwin et Tim1'], 'current': 0, 'board': [[0], [1,8,9]]}}


lb=dico['state']['board'][0]
lw=dico['state']['board'][1]
player=dico['state']['current']

if player ==0:
    print("je suis noir")
if player==1:
    print("je suis blanc")

def winner(lb,lw):
    if len(lb)>len(lw):
        return 0
    if len (lb)<len(lw):
        return 1

def gameover(lb,lw):
    #le jeu se termine si aucun des deux joueurs ne peut jouer un coup ou si le terrai est rempli
    if len(lb)+len(lw)==64:
        return True
    return False


def utility(lb,lw, player):
	theWinner = winner(lb,lw)
	if theWinner is None:
		return 0
	if theWinner == player:
		return 1
	return -1

def apply(lb,lw,i,j,coup,player):
    #return le plateau transformé après le coup
    if player==0: #black
        
        
        pass


print(gameover(lb,lw))



