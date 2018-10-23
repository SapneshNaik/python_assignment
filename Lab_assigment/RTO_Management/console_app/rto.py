import sys
import mysql.connector
from prettytable import PrettyTable

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
            print(PrettyTable(results))
        except Exception as e:
            print(e)
            print( "\n WARNING: could not print table \n")

        finally:
            mycursor.close()

    def get_all_RTO(conn):

        mycursor = conn.cursor()
        try:
            mycursor.execute("SELECT * FROM RTO_DB.rto_details")
            myresult = mycursor.fetchall()
            pt = PrettyTable([i[0] for i in mycursor.description])

            pt.align= "l"

            for row in myresult:
                pt.add_row(row)

            print(pt)


        except Exception as e:
            print(e)
            print( "\n WARNING: could not print table \n")

        finally:
            mycursor.close()


    def init_db(conn):

        mycursor = conn.cursor()
        try:
            mycursor.execute("CREATE DATABASE IF NOT EXISTS RTO_DB")
            mycursor.execute("CREATE TABLE IF NOT EXISTS RTO_DB.rto_details (ID INT(10) PRIMARY KEY, RTOINCHARGE VARCHAR(255), Designation VARCHAR(255), PLACE VARCHAR(255))")
            mycursor.execute("CREATE TABLE IF NOT EXISTS RTO_DB.user_registrations (USERID INT(10) PRIMARY KEY, USERNAME VARCHAR(255), VEHICLETYPE VARCHAR(255), VEHICLENO INT(4) UNIQUE, VEHICLECOLOR VARCHAR(255))")
            
        except Exception as e:
            print(e)
            print( "\n There was an error initializing RTO database and tables")
            sys.exit()

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
                print("\n Success: RTO Registration Successful \n")

            except mysql.connector.Error as err:
                if err.errno == 1062:
                    print("\n Error: ID already exists plase try with a different ID \n")
                    sys.exit()

        except Exception as e:
            print(e)
            print( "\n Error persisiting")
            sys.exit()

        finally:
            mycursor.close()