Le programme DERNIERE_VERSION est un IA qui a été spécialement designée pour le jeu de othello de mr. Lurkin
La stratégie est très simple: l'IA joue le coup qui retourne le plus de pions adverse

La grande particularité de notre programme est d'avoir nous-mêmes crée le système de détection de coup possible en fonction
de la lecture du board dans le fichier json reçu par le serveur hôte de partie. Ce programme est visible dans le fichier "aveclesbords.py"
Il consite en un appel de fonction récursive propre à chaque couleur. Gérer les bords n'a pas été facile.

Le fichier homemade strategy.py contient notre ... stratégie. Encore une fois nous avons nous-mêmes crée la fonction
qui return le nombre de pions retourné de le l'ennemi en fonction du coup joué.
On l'a alors associé aux fonctions qui return les listes des coups possibles
Enfin on compare les coups et on garde le meilleur sous forme de dictionnaire

Le fichier Inscription1.json contient nos données d'inscription

Le fichier move.json est le message que l'onenvoie au serveur hôte

Le fichier test_DERNIERE_VERSION.py teste notre couverture de code, qui est de 80%
