import logging
from random import randint
import mysql.connector
import sys
from prettytable import PrettyTable
logging.basicConfig(filename='user.log',level=logging.ERROR)

class User:
    def __init__(self, USERID, USERNAME, VEHICLETYPE, VEHICLENO, VEHICLECOLOR):
        self.USERID = USERID
        self.USERNAME = USERNAME    
        self.VEHICLETYPE = VEHICLETYPE
        self.VEHICLENO = VEHICLENO
        self.VEHICLECOLOR = VEHICLECOLOR


    def get_User(self, conn ,USERID):
        mycursor = self.conn.cursor()
        try:
            mycursor.execute("SELECT * FROM RTO_DB.user_registrations WHERE USERID=%s", (self.USERID))
            myresult = mycursor.fetchall()
            for x in myresult:
              print(x)

        except Exception as e:
            print(e)
            print( "\n WARNING: could not print table \n")

        finally:
            mycursor.close()


    def get_all_users(conn):
        mycursor = conn.cursor()
        try:
            mycursor.execute("SELECT * FROM RTO_DB.user_registrations")
            myresult = mycursor.fetchall()
            return myresult

        except Exception as e:
            print(e)
            print( "\n WARNING: could not print table \n")

        finally:
            mycursor.close()

    #generate a 4 digit random vehicle number which is not already taken
    def get_new_vehicle_number(conn):
        rand = randint(1000, 9999) #4 digit random number
        mycursor = conn.cursor()
        try:
            exists = True
            while not exists:
                sql= "SELECT * FROM RTO_DB.user_registrations WHERE VEHICLENO="+str(rand)
                mycursor.execute(sql)
                if mycursor.rowcount == -1:
                    exists = False

            return rand

        except Exception as e:
            print(e)
            print( "\n WARNING: could not generate vehicle number \n")

        finally:
            mycursor.close()




    def persist(self, conn):

        mycursor = conn.cursor()
        try:
            sql = "INSERT INTO RTO_DB.user_registrations (USERID, USERNAME, VEHICLETYPE, VEHICLENO, VEHICLECOLOR) VALUES (%s, %s, %s, %s, %s)"
            val = (self.USERID, self.USERNAME, self.VEHICLETYPE, self.VEHICLENO, self.VEHICLECOLOR)
            try:
                mycursor.execute(sql, val)
                conn.commit()
                mycursor.close()
                return True
            except mysql.connector.Error as err:
                if err.errno == 1062:
                    logging.error("user id exists")
                    logging.error(err)
                    return False

        except Exception as e:
            logging.error("persist")
            logging.error(e)
            return False
            