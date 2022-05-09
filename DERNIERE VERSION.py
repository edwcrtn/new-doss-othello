import socket
import json
import random

ipserver="localhost"
#ipserver="172.17.10.33"
hisserverAddress=(ipserver,3000)    #adresse de l'hôte du serveur

bord=[0,1,2,3,4,5,6,7,15,23,31,39,47,55,63,62,61,60,59,58,57,56,48,40,32,24,16,8] 
bordg=[0,8,16,24,32,40,48,56]     #bord gauche
bordd=[7,15,23,31,39,47,55,63]      #bord droit


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



def inscription():                                                 #fonction de depart qui se connecte au serveur de jeu et s'inscript
    with open ("inscription1.json","r") as file:   
        data=file.read()                                           #contient les donnée d'inscription
    with socket.socket() as s:     
        s.connect(hisserverAddress)
        s.send(data.encode())
        response=json.loads(s.recv(2048).decode())   
        print(response)
        server()

def server():                                                      #fonction qui tourne en boucle
    with socket.socket() as s:
        myserverAddress=('0.0.0.0',8887)                           #renvoie pong quand reçoit ping
        s.bind(myserverAddress)                                    #renvoie un coup quand on lui en demande un
        s.listen()
        pong={"response": "pong"}
        ping={"request": "ping"}
        
        while True:
            jeu, address=s.accept()
            message=json.loads(jeu.recv(2048).decode())
            print(message)
            if message==ping:
                jeu.send(json.dumps(pong).encode())
                print(pong)
            else:
                if message['request']=='play':
                    lb=message['state']['board'][0]          #liste des index des noirs
                    lw=message['state']['board'][1]          #liste des index des blancs
                    
                    if message['state']['current']==0:
                        if cpb(lb,lw)==[]:
                            case='null'
                        else:
                            case=random.choice(cpb(lb,lw))
                        
                    if message['state']['current']==1:
                        if cpw(lb,lw)==[]:
                            case='null'
                        else:
                            case=random.choice(cpw(lb,lw))

                    filename="move.json"
                    jsonstring='{"response": "move","move": '
                    
                    jsonstring+=str(case)+','
                    jsonstring+='"message": "'+str(case)+'"}'  
                    data=json.loads(jsonstring)
                    file=open(filename,'w')
                    json.dump(data,file)
                    with open("move.json","r") as file:
                        data=file.read() 
                    jeu.send(data.encode())
                    print(data)
                       

inscription()