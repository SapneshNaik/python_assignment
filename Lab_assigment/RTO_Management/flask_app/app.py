from flask import Flask, json, render_template, request
import sys
sys.path.insert(0, 'models')
from rto import RTO
from user import User
import mysql.connector
global conn

conn = mysql.connector.connect(host="localhost", user="root",password="root")


app = Flask(__name__)



#home page route by default GET
@app.route("/")
def main():
    #init db on home page visit
    RTO.init_db(conn)
    return render_template('index.html')

#Route to show new RTO registration form
@app.route('/RTO/register')
def newRTORegForm():
    return render_template('rto_form.html')


#Route to show new User registration form
@app.route('/User/register')
def newUserRegForm():
    return render_template('user_form.html')


#Route for new RTO registration
@app.route('/RTO/persist',methods=['POST'])
def newRTOReg():
    # read the posted values from the UI
    _RTOID = request.form['RTOID']
    _RTOINCHARGE = request.form['RTOINCHARGE']
    _Designation = request.form['Designation']
    _Location = request.form['Location']

    new_rto = RTO(_RTOID, _RTOINCHARGE, _Designation, _Location)
    if new_rto.persist(conn):
        return json.dumps({'message':'RTO registration successful !'})
    else:
        return json.dumps({'message':'Failed. ID already taken!'})


#Route for new RTO registration
@app.route('/User/persist',methods=['POST'])
def newUserReg():
    # read the posted values from the UI
    _UserID = request.form['UserID']
    _UserName = request.form['UserName']
    _VehicleType = request.form['VehicleType']
    _VehicleColor = request.form['VehicleColor']
    _VEHICLENO = User.get_new_vehicle_number(conn)

    new_vehicle = User(_UserID, _UserName, _VehicleType, _VEHICLENO, _VehicleColor)
    if new_vehicle.persist(conn):
        return json.dumps({'message':'RTO registration successful !', 'Number': _VEHICLENO})
    else:
        return json.dumps({'message':'Failed. User ID already taken!'})


@app.route('/RTO/list')
def listRTOs():
    # read the posted values from the UI
    RTOs = RTO.get_all_RTO(conn)
    return render_template('rto_table.html', result = RTOs)



@app.route('/User/list')
def listUsers():
    # read the posted values from the UI
    users = User.get_all_users(conn)
    return render_template('user_table.html', result = users)

if __name__ == "__main__":
    app.run()