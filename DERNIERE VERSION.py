import socket
import json
import random

ipserver="localhost"
hisserverAddress=(ipserver,3000)    #adresse de l'hôte du serveur
bord=[0,1,2,3,4,5,6,7,15,23,31,39,47,55,63,62,61,60,59,58,57,56,48,40,32,24,16,8]

def recursifb(lb,lw,cp,i,j,a):
    if i+j in lb and i+j*a in lw and i+j*a in bord:
        return None

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
                if v>0 and v<64:
                    cpo.append(v)
    return cpo


def recursifw(lb,lw,cp,i,j,a):
    if i+j in lb and i+j*a in lb and i+j*a in bord:
        return None
    
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
                if v>0 and v<64:
                    cpo.append(v)
    return cpo

def inscription():

    with open ("inscription1.json","r") as file:   
        data=file.read()                      #contient les donnée d'inscription
    with socket.socket() as s:     
        s.connect(hisserverAddress)
        s.send(data.encode())
        response=json.loads(s.recv(2048).decode())   
        #print(response)
        server()

def server():
    with socket.socket() as s:
        myserverAddress=('0.0.0.0',8887)
        s.bind(myserverAddress)
        s.listen()
        pong={"response": "pong"}
        ping={"request": "ping"}
        
        while True:
            jeu, address=s.accept()
            message=json.loads(jeu.recv(2048).decode())
            print(message)
            if message==ping:
                jeu.send(json.dumps(pong).encode())
                #print(pong)
            else:
                if message['request']=='play':
                    lb=message['state']['board'][0]
                    #print(lb)
                    lw=message['state']['board'][1]
                    #print(lw)
                    
                    if message['state']['current']==0:
                        #print("Coups possibles pour les noirs : ")
                        #print(cpob(lb,lw))
                        case=random.choice(cpob(lb,lw))

                    if message['state']['current']==1:
                        #print("Coups possibles pour les blancs : ")
                        #(cpow(lb,lw))
                        case=random.choice(cpow(lb,lw))




                    filename="move.json"
                    jsonstring='{"response": "move","move": '
                    
                    #case=input("Sur quelle case jouer? ")
                    jsonstring+=str(case)+','
                    jsonstring+='"message": "'+str(case)+'"}'  #"Fun message"}'
                    data=json.loads(jsonstring)
                    file=open(filename,'w')
                    json.dump(data,file)
                    with open("move.json","r") as file:
                        data=file.read() 
                    print("vies : ",message['lives'])
                    jeu.send(data.encode())
                    print(data)
                
        

inscription()