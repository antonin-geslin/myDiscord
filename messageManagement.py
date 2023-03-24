
import mysql
import mysql.connector

class MessageManagement():


    def __init__(self, user, password, database, host='localhost'):
        self.user = user
        self.password = password
        self.database = database
        self.host = host
        self.connexion = mysql.connector.connect(user=self.user, password=self.password, host=self.host, database=self.database)
        self.cursor = self.connexion.cursor()



    def addMessageToBdd(self, user, message):
        query = ("INSERT INTO messages (user, message) VALUES (%s, %s)")
        values = (user, message)
        self.cursor.execute(query, values)
        self.connexion.commit()
        return self.cursor.lastrowid

    def getAllMessages(self):
        query = ("SELECT user, message FROM messages")
        self.cursor.execute(query)
        return(self.cursor.fetchall())
    
