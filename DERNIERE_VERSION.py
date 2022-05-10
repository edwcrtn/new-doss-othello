import socket
import json
import random

ipserver="localhost"
#ipserver="172.17.10.33"
port=3000
hisserverAddress=(ipserver,port)
myserveraddress='0.0.0.0',8887    #adresse de l'hôte du serveur
pong={"response": "pong"}
ping={"request": "ping"}

bord=[0,1,2,3,4,5,6,7,15,23,31,39,47,55,63,62,61,60,59,58,57,56,48,40,32,24,16,8] 
bordg=[0,8,16,24,32,40,48,56]     #bord gauche
bordd=[7,15,23,31,39,47,55,63]      #bord droit

#TROUVER LES COUPS
def recursifb(lb,lw,cp,i,j,a,b):                                    #fonction recursive qui retourne la case sur laquelle peut jouer le joueur noir pour une certaine case de départ
    if i+j*(a-2) in bordd and j in [-7,+1,+9]:                      #et une certaine direction j    renvoie None si pas de coup possible
        return None                                                 #ma petite fierté cette fonction
    if i+j*(a-2) in bordg and j in [-9,-1,+7]:
        return None
    if i+j*b in lw and i+j*a not in cp and i+j*a not in lb and i+j*a not in lw :
        if i+j*b in bordd and j in [-7,+1,+9]:
            return None
        if i+j*b in bordg and j in [-9,-1,+7]:
            return None  
        return i+j*a
    if i+j*b in lw and i+j*a not in cp and i+j*a not in lb and i+j*a in lw:
        a+=1
        b+=1
        return(recursifb(lb,lw,cp,i,j,a,b))


def cpb(lbl,lwh):                                                  #fonction qui appelle la fonction récursive de la couleur associée (noir) 
    cpo=[]                                                         #pour chaque case noir elle appelle la fonction recursive
    for i in lbl:                                                  #et l'ajoute à la liste de coup possible cpo
        for j in (-9,-8,-7,-1,+1,+7,+8,+9):
            if recursifb(lbl,lwh,cpo,i,j,2,1) != None:
                v=recursifb(lbl,lwh,cpo,i,j,2,1)
                if v in range(64):
                    cpo.append(v)
    return cpo

def recursifw(lb,lw,cp,i,j,a,b):                                  #meme principe mais pour les blancs
    if i+j*(a-2) in bordd and j in [-7,+1,+9]:
        return None
    if i+j*(a-2) in bordg and j in [-9,-1,+7]:
        return None    
    if i+j*b in lb and i+j*a not in cp and i+j*a not in lw and i+j*a not in lb:
        if i+j*b in bordd and j in [-7,+1,+9]:
            return None
        if i+j*b in bordg and j in [-9,-1,+7]:
            return None
        return i+j*a
    if i+j*b in lb and i+j*a not in cp and i+j*a not in lw and i+j*a in lb:
        a+=1
        b+=1
        return(recursifw(lb,lw,cp,i,j,a,b))
    

def cpw(lbl,lwh):
    cpo=[]
    for i in lwh:
        for j in (-9,-8,-7,-1,+1,+7,+8,+9):
            if recursifw(lbl,lwh,cpo,i,j,2,1) != None:
                v=recursifw(lbl,lwh,cpo,i,j,2,1)
                if v in range(64):
                    cpo.append(v)
    return cpo

#ANALYSER LES COUPS
def pionsprisb(lw,lb,coup,j,a=2,b=1):
    case = coup 
    if case+j*a not in range(64):
        return None
    if case+j*a not in lw and case+j*a not in lb:
        return None
    if case+j*a in lb:
        return b
    else:
        a+=1
        b+=1
        return(pionsprisb(lw,lb,coup,j,a,b))

def bestb(lb,lw):                                                    #renvoie le coup qui prend le plus de pion d'un coup
    max={"coup":None,"points":0}
    for coup in cpb(lb,lw):
        for j in (-9,-8,-7,-1,+1,+7,+8,+9):
            if pionsprisb(lw,lb,coup,j) !=None:
                if pionsprisb(lw,lb,coup,j)>max["points"]:
                    max["coup"]=coup
                    max["points"]=pionsprisb(lw,lb,coup,j)
    return max["coup"]


def pionsprisw(lw,lb,coup,j,a=2,b=1):
    case = coup 
    if case+j*a not in range(64):
        return None
    if case+j*a not in lw and case+j*a not in lb:
        return None
    if case+j*a in lw:
        return b
    else:
        a+=1
        b+=1
        return(pionsprisw(lw,lb,coup,j,a,b))

def bestw(lb,lw):                                                    #renvoie le coup qui prend le plus de pion d'un coup
    max={"coup":None,"points":0}
    for coup in cpw(lb,lw):
        for j in (-9,-8,-7,-1,+1,+7,+8,+9):
            if pionsprisw(lw,lb,coup,j) !=None:
                if pionsprisw(lw,lb,coup,j)>max["points"]:
                    max["coup"]=coup
                    max["points"]=pionsprisw(lw,lb,coup,j)
    return max["coup"]

#LANCEMENT
def inscription():                                                 #fonction de depart qui se connecte au serveur de jeu et s'inscript
    with open ("inscription1.json","r") as file:   
        data=file.read()                                           #contient les donnée d'inscription
    with socket.socket() as s:     
        s.connect(hisserverAddress)
        s.send(data.encode())  
        server()

def server():                                                      #fonction qui tourne en boucle
    with socket.socket() as s:                                    #renvoie pong quand reçoit ping
        s.bind(myserveraddress)                                    #renvoie un coup quand on lui en demande un
        s.listen() 
        while True:
            jeu, address=s.accept()
            message=json.loads(jeu.recv(2048).decode())
            if message==ping:
                jeu.send(json.dumps(pong).encode())
            else:
                if message['request']=='play':
                    lb=message['state']['board'][0]          #liste des index des noirs
                    lw=message['state']['board'][1]          #liste des index des blancs  
                    if message['state']['current']==0:
                        if cpb(lb,lw)==[]:
                            case='null'
                        else:
                            case=bestb(lb,lw)                       
                    if message['state']['current']==1:
                        if cpw(lb,lw)==[]:
                            case='null'
                        else:
                            case=bestw(lb,lw)
                    jsonstring='{"response": "move","move": ' + str(case) +',' + '"message": "'+str(case)+'"}'           
                    data=json.loads(jsonstring)
                    file=open("move.json",'w')
                    json.dump(data,file)
                    with open("move.json","r") as file:
                        data=file.read() 
                    jeu.send(data.encode())

                       
if __name__ == "__main__":
    inscription()