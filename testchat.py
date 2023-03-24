import socket
import threading
import tkinter as tk
import sys
from messageManagement import * 
import json 

bd2 = MessageManagement("discord", "abcdeABCDE;12345", "mydiscord")

class Client:
    def __init__(self, host, port):
        self.host = '127.0.0.1'
        self.port =     50000
        self.connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.input_texte = None
        self.messages_listbox = None
        self.connected_users_listbox = None

    def connect(self):
        try:
            self.connexion.connect((self.host, self.port))
        except socket.error:
            print("La connexion a échoué.")
            sys.exit()
        print("Connexion établie avec le serveur.")

    def send_message(self):
        with open('messages.json', 'r') as f:
            data = json.load(f)
        message = self.input_texte.get()
        message2 = self.input_texte.get()
        self.connexion.send(message.encode())
        self.input_texte.delete(0, tk.END)
        self.messages_listbox.insert(tk.END, message)
        bd2.addMessageToBdd(data[-1]['user'], message2)


    def receive_messages(self):
        while True:
            message =  self.connexion.recv(1024).decode()
            if self.messages_listbox and self.messages_listbox.size():
                self.messages_listbox.insert(tk.END, message)


    def start(self):
        self.connect()
        thread_reception = threading.Thread(target=self.receive_messages)
        thread_reception.start()
        fenetre = ChatWindow(self)
        fenetre.mainloop()
        self.connexion.close()




class ChatWindow(tk.Tk):
    def __init__(self, client):
        tk.Tk.__init__(self)
        self.client = client
        self.title("Client Chat")
        self.create_widgets()

    def create_widgets(self):
        # création de la liste des messages
        messages_frame = tk.Frame(self)
        messages_scrollbar = tk.Scrollbar(messages_frame)
        messages_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.client.messages_listbox = tk.Listbox(messages_frame, height=25, width=100, yscrollcommand=messages_scrollbar.set)
        self.client.messages_listbox.pack(side=tk.LEFT, fill=tk.BOTH)
        messages_frame.pack(side=tk.LEFT, padx=10)
        for row in bd2.getAllMessages():
           self.client.messages_listbox.insert(tk.END, row[0] + " : " + row[1])


        # création de la liste des utilisateurs connectés
        connected_users_frame = tk.Frame(self)
        connected_users_label = tk.Label(connected_users_frame, text="Utilisateurs connectés : ")
        connected_users_label.pack(side=tk.TOP)
        connected_users_scrollbar = tk.Scrollbar(connected_users_frame)
        connected_users_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.client.connected_users_listbox = tk.Listbox(connected_users_frame, height=25, width=25, yscrollcommand=connected_users_scrollbar.set)
        self.client.connected_users_listbox.pack(side=tk.LEFT, fill=tk.BOTH)
        connected_users_frame.pack(side=tk.RIGHT, padx=10, pady=10)

        # création de la zone de saisie de texte et de la liste des salons
        input_frame = tk.Frame(self)
        self.client.input_texte = tk.Entry(input_frame, width=50)
        self.client.input_texte.pack(side=tk.LEFT)
        input_bouton = tk.Button(input_frame, text="Envoyer", command=self.client.send_message)
        input_bouton.pack(side=tk.RIGHT)
        input_frame.pack(side=tk.LEFT, padx=10, pady=10)

        # création de la liste des salons
        salons_frame = tk.Frame(self)
        salons_label = tk.Label(salons_frame, text="Salons disponibles")
        salons_label.pack()
        salons_scrollbar = tk.Scrollbar(salons_frame)
        salons_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.salons_listbox = tk.Listbox(salons_frame, height=20, width=20, yscrollcommand=salons_scrollbar.set)
        self.salons_listbox.pack(side=tk.LEFT, fill=tk.BOTH)
        salons_frame.pack(side=tk.RIGHT, padx=10, pady=10)


if __name__ == "__main__":
    client = Client("localhost", 50000)
    client.start()