import socket
import json

ipserver="localhost"
hisserverAddress=(ipserver,3000)    #adresse de l'hôte du serveur

def inscription():

    with open ("inscription1.json","r") as file:   
        data=file.read()                      #contient les donnée d'inscription
    with socket.socket() as s:     
        s.connect(hisserverAddress)
        s.send(data.encode())
        response=json.loads(s.recv(2048).decode())   
        print(response)
        pong()

def pong():
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
                print(pong)
            else:
                if message['request']=='play':
                    liste_black=message['state']['board'][0]
                    print(liste_black)
                    liste_white=message['state']['board'][1]
                    print(liste_white)
                    filename="move.json"
                    jsonstring='{"response": "move","move": '
                    case=input("Sur quelle case jouer? ")
                    jsonstring+=str(case)+','
                    jsonstring+='"message": "'+str(case)+'"}'  #"Fun message"}'
                    data=json.loads(jsonstring)
                    file=open(filename,'w')
                    json.dump(data,file)
                    with open("move.json","r") as file:
                        data=file.read() 
                    jeu.send(data.encode())
                    print(data)
                
        

inscription()