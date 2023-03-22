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
        query = ("INSERT INTO user (nom, prenom, mail, password) VALUES (%s, %s, %s, %s)")
        values = (nom, prenom, mail, password)
        self.cursor.execute(query, values)
        self.connexion.commit()

    def userConnexion(self, mail, password):
        query = ("SELECT * FROM user WHERE mail = %s AND password = %s")
        values = (mail, password)
        self.cursor.execute(query, values)
        result = self.cursor.fetchall()
        if result:
            return True
        else:
            return False


    def get_username(self, user):
        self.user = user
        return self.user