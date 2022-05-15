#AUTEURS
Edwin Creten 20220 et Timothé Couturier 20091

#RECURSIVINATOR

Le programme DERNIERE_VERSION est un IA qui a été spécialement designée pour le jeu de othello de mr. Lurkin

La stratégie est la suivante : les 17 premiers coups l'IA joue le meilleur coup possible en fonction du poids de la case.  
Ensuite l'IA joue le coup qui retourne le plus de pions adverse mais joue toujours dans les coins en priorié. 
Cela permet de prendre des cases stratégiques dans un premier temps,puis de raffler les pions adverese dans un deuxième temps
L'ia aléatoire se fait OBLITERER en 1v1 pûr dans les règles

image.png

La grande particularité de notre programme est d'avoir nous-mêmes créé le système de détection de coups possibles en fonction de la lecture du board dans le fichier json reçu par le serveur hôte de partie. Ce programme est visible dans le fichier "aveclesbords.py"
Il consite en un appel de fonction récursive propre à chaque couleur. Gérer les bords n'a pas été facile.

Le fichier homemade strategy.py contient notre ... stratégie. Encore une fois nous avons nous-mêmes crée la fonction qui return le nombre de pions retournés de le l'ennemi en fonction du coup joué.
On l'a alors associé aux fonctions qui return les listes des coups possibles
Enfin on compare les coups et on garde le meilleur sous forme de dictionnaire.
Tout est alors traduit en fichier json et envoyé au serveur hôte.

Le fichier Inscription1.json contient nos données d'inscription

Le fichier move.json est le message que l'on envoie au serveur hôte

Le fichier test_DERNIERE_VERSION.py teste notre couverture de code, qui est de 83%

Tous les commentaires explicatifs sont dans le fichier principal DERNIERE_VERSION.py

#POUR CHANGER LE PORT :
Il faut changer le numéro dans le fichier "Inscription1.json" et mettre le même à la ligne 9 du fichier "DERNIERE_VERSION.py"
Le port est 8887 par défaut