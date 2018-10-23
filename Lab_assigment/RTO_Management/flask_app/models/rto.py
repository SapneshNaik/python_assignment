import logging
import sys
import mysql.connector
from prettytable import PrettyTable
logging.basicConfig(filename='rto.log',level=logging.ERROR)

class RTO:
    def __init__(self, ID, RTOINCHARGE, Designation, PLACE):
        self.ID = ID
        self.RTOINCHARGE = RTOINCHARGE    
        self.Designation = Designation
        self.PLACE = PLACE


    def get_RTO(self, conn ,ID):

        mycursor = self.conn.cursor()
        try:
            mycursor.execute("SELECT * FROM RTO_DB.rto_details WHERE ID=%s", (self.ID))
            results = mycursor.fetchall()
            # print(PrettyTable(results))
        except Exception as e:
            logging.error("get_RTO")
            logging.error(e)
            # print( "\n WARNING: could not print table \n")
        finally:
            mycursor.close()

    def get_all_RTO(conn):

        mycursor = conn.cursor()
        try:
            mycursor.execute("SELECT * FROM RTO_DB.rto_details")
            myresult = mycursor.fetchall()
            return myresult


        except Exception as e:
            print(e)
            # print( "\n WARNING: could not print table \n")

        finally:
            mycursor.close()


    def init_db(conn):
        logging.error("init_db execute")

        mycursor = conn.cursor()
        try:
            mycursor.execute("CREATE DATABASE IF NOT EXISTS RTO_DB")
            mycursor.execute("CREATE TABLE IF NOT EXISTS RTO_DB.rto_details (ID INT(10) PRIMARY KEY, RTOINCHARGE VARCHAR(255), Designation VARCHAR(255), PLACE VARCHAR(255))")
            mycursor.execute("CREATE TABLE IF NOT EXISTS RTO_DB.user_registrations (USERID INT(10) PRIMARY KEY, USERNAME VARCHAR(255), VEHICLETYPE VARCHAR(255), VEHICLENO INT(4) UNIQUE, VEHICLECOLOR VARCHAR(255))")
            
        except Exception as e:
            logging.error("init_db")
            logging.error(e)

        finally:
            mycursor.close()


    def persist(self, conn):

        mycursor = conn.cursor()
        try:
            sql = "INSERT INTO RTO_DB.rto_details (ID, RTOINCHARGE, Designation, PLACE) VALUES (%s, %s, %s, %s)"
            val = (self.ID, self.RTOINCHARGE, self.Designation, self.PLACE)
            
            try:
                mycursor.execute(sql, val)
                conn.commit()
                return True

            except mysql.connector.Error as err:
                if err.errno == 1062:
                    logging.error("persist execute")
                    logging.error(err)

                return False                   

        except Exception as e:
            logging.error("persist")
            logging.error(e)
            return False                   

        finally:
            mycursor.close()