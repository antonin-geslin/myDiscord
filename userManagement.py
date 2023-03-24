import mysql.connector
import mysql

class userManagement():

    def __init__(self, user, password, database, host='localhost'):
        self.user = user
        self.password = password
        self.database = database
        self.host = host
        self.connexion = mysql.connector.connect(user=self.user, password=self.password, host=self.host, database=self.database)
        self.cursor = self.connexion.cursor()


    def userInscription(self, nom, prenom, mail, password):
        print(f"Inserting user: nom={nom}, prenom={prenom}, mail={mail}, password={password}")
        query = ("INSERT INTO user (nom, prenom, mail, password) VALUES (%s, %s, %s, %s)")
        values = (nom, prenom, mail, password)
        self.cursor.execute(query, values)
        self.connexion.commit()

    def checkIfUserExist(self, mail):
        query = f"SELECT * FROM user WHERE mail = '{mail}'"
        self.cursor.execute(query)
        return(self.cursor.fetchall())

    def checkUserPassword(self, mail):
        query = f"SELECT password FROM user WHERE mail = '{mail}'"
        self.cursor.execute(query)
        return(self.cursor.fetchall()[0][0])


