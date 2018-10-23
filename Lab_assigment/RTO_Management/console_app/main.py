from rto import RTO
from user import User
import mysql.connector
global conn

conn = mysql.connector.connect(host="localhost", user="root",password="root")

def connection():
    
    if conn.is_connected():
        return True
    else:
        return False

def show_choices():
    print(" 1 - Register a new RTO")      
    print(" 2 - Register a new Vehicle")       
    print(" 3 - Diplay RTOs")
    print(" 4 - Display User Details")      
    print(" 5 - Quit")

def valid_choice(choice):
    return True if (choice >= 1) and (choice <= 5) else False

def main():

    show_choices()

    choice = None


    print("\nIntializing the application...")
    RTO.init_db(conn)
    print("Done")
    
    while choice is not 5:

        try:
            choice = int(input("\nEnter choice\n"))

            #check if valid choice
            if not valid_choice(choice):
                print("Invalid choice")
                continue

            if choice == 5:
                print("\nBye\n")
                break
        except:
            print("Invalid number.. ")
            continue


        if choice is 1:
            try:
                ID = int(input("Enter new RTO ID (number):\t"))
            except Exception as e:
                print("Error: ID must be an integer\t")
                continue

            RTOINCHARGE = input("Enter RTO Incharge name:\t")
            Designation = input("Enter RTO Incharge Designation:\t")
            PLACE = input("Enter RTO location:\t")

            new_rto = RTO(ID, RTOINCHARGE, Designation, PLACE)

            new_rto.persist(conn)
            RTO.get_all_RTO(conn)


        if choice is 2:
            try:
                USERID = int(input("Enter new User ID (number):\t"))
            except Exception as e:
                print("Error: User ID must be an integer\t")
                continue

            USERNAME = input("Enter new User name:\t")

            VEHICLETYPE = input("Enter new Vehicle type:\t")

            VEHICLENO = User.get_new_vehicle_number(conn)

            VEHICLECOLOR = input("Enter Vehicle color:\t")

            new_vehicle = User(USERID, USERNAME, VEHICLETYPE, VEHICLENO, VEHICLECOLOR)
            new_vehicle.persist(conn)
            User.get_all_users(conn)

        if choice is 3:
            print("\n RTO Details \n")
            RTO.get_all_RTO(conn)

        if choice is 4:
            print("\n User Details \n")
            User.get_all_users(conn)

    conn.close()
if __name__ == "__main__":
    main()