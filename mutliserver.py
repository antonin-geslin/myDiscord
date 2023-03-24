#Definition serveur réseau gerant un systeme CHAT simplifié.
#Utilise les threads pour gérer les connexions clientes en parallèle.

import socket, sys, threading
import json
import userManagement

HOST = '127.0.0.1'
PORT = 50000

salons = {"salon1":[], "salon2":[], "salon3":[]}

class ThreadClient(threading.Thread):
    '''dérivation d'un objet thread pour gérer la connexion avec un client'''
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.connexion = conn
    

        #ref du socket de connexion

        
    def run(self):
        #Dialogue avec le client 
        nom = self.getName()

        with open('messages.json', 'r') as f:
            data = json.load(f)
            mail = data[-1]['user']
        
        #Chaque thread possède un nom
        while True:
            msgClient = self.connexion.recv(1024).decode("Utf8") 
            if not msgClient or msgClient.upper() == "FIN" :
                break
            message = "%s : %s" %(mail, msgClient)
            print(message)
        # Faire suivre le message à tous les autres clients :
            for cle in list(conn_client):
                if cle != nom:
                #ne pas le renvoyer a l'émetteur
                    conn_client[cle].send(message.encode("Utf8"))
        self.connexion.close()
        del conn_client[nom]
        print("Client %s déconnecté." %nom)

#initialisation du serveur - mise en place du scoket: 
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    mySocket.bind((HOST, PORT))
except socket.error:
    print("La laisaison du socket à l'adresse choisie a échoué")
    sys.exit()
print("Serveur prêt, en attente de requêtes...")
mySocket.listen(5)


#attente et prise en charge des connexions demandées par les clients :
conn_client = {}

while 1:
    connexion, adresse = mySocket.accept()
    #créer un nouvel objet tread pour gérer la connexion:
    th = ThreadClient(connexion)
    th.start()
    #mémoriser la connexion dans le dictionnaire:
    it = th.getName() #identifiant du thread
    conn_client[it] = connexion
    print("Client %s connecté, adresse IP %s, port %s." %\
          (it, adresse[0], adresse[1]))
    
    #dialgue avec le client:
    msg = "Vous êtes connecté.envoyez vos messages."
    connexion.send(msg.encode("Utf8"))

