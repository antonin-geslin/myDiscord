from tkinter import *
from tkinter import ttk
from userManagement import userManagement

bdd = userManagement('root', '*******', 'mydiscord')

def inscription(frame1,frame2):

    frame1.pack_forget()
    return frame2.pack()


def returnToConnexion(frame1, frame2):
    nom = entrerNom.get()
    prenom = entrerPrenom.get()
    mail = entrerMail.get()
    password = entrerMdp.get()
    bdd.userInscription(nom, prenom, mail, password)
    frame2.pack_forget()
    return frame1.pack()



fenetre=Tk()
fenetre.title("myDiscord")
fenetre.geometry("900x900")


frame2 = Frame(fenetre, width=900, height=900)
frame2.pack()
labelTitre = Label(frame2, text = "myDiscord", font=('Arial', 50))
labelTitre.place(x=330,y=50)
labelInscription = Label(frame2, text = "Inscription", font=('Arial', 20))
labelInscription.place(x=400,y=200)
labelNom = Label(frame2, text = "Nom", font=('Arial', 15))
labelNom.place(x=250,y=300)
entrerNom = Entry(frame2)
entrerNom.place(x=350,y=300,width=300, height=30)
labelPrenom = Label(frame2, text = "Prenom", font=('Arial', 15))
labelPrenom.place(x=250,y=350)
entrerPrenom = Entry(frame2)
entrerPrenom.place(x=350,y=350,width=300, height=30)
labelMail = Label(frame2, text = "Mail", font=('Arial', 15))
labelMail.place(x=250,y=400)
entrerMail = Entry(frame2)
entrerMail.place(x=350,y=400,width=300, height=30)
labelMdp = Label(frame2, text = "Password", font=('Arial', 15))
labelMdp.place(x=250,y=450)
entrerMdp = Entry(frame2)
entrerMdp.place(x=350,y=450,width=300, height=30)
buttonInscription = Button(frame2, text = "Inscription", font=('Arial', 15), command=lambda: returnToConnexion(frame1, frame2))
buttonInscription.place(x=350, y= 500, width=300)
frame2.pack_forget()


frame1 = Frame(fenetre, width=900, height=900)
frame1.pack()
labelTitre = Label(frame1, text = "myDiscord", font=('Arial', 50))
labelTitre.place(x=330,y=50)
labelConnexion = Label(frame1, text = "Connexion", font=('Arial', 20))
labelConnexion.place(x=400,y=200)
labelMail = Label(frame1, text = "Mail", font=('Arial', 15))
labelMail.place(x=250,y=300)
entrerMail = Entry(frame1)
entrerMail.place(x=350,y=300,width=300, height=30)
labelMdp = Label(frame1, text = "Password", font=('Arial', 15))
labelMdp.place(x=250,y=350)
entrerMdp = Entry(frame1, show="*")
entrerMdp.place(x=350,y=350,width=300, height=30)
buttonConnexion = Button(frame1, text = "Connexion", font=('Arial', 15), command=fenetre.destroy)
buttonConnexion.place(x=350, y= 400, width=300)

LabelInscription = Label(frame1, text = "Pas encore inscrit ?", font=('Arial', 10))
LabelInscription.place(x=400,y=440)
buttonInscription = Button(frame1, text = "Cliquez ici !", font=('Arial', 10), command=lambda: inscription(frame1, frame2))
buttonInscription.place(x=490, y= 437)




fenetre.mainloop()

fenetre2=Tk()
fenetre2.title("myDiscord")
fenetre2.geometry("900x900")
fenetre2.mainloop()