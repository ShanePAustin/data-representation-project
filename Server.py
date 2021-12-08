#Flask server application for Data Representation Project 2021
#Author: Shane Austin
##########################################################################################################
##########################################################################################################

from flask import Flask, url_for, request, redirect, abort, jsonify, render_template, session, g, session
from RNLIDao import rnliDao
from rnliScrapeCSV import getStations, getFleet

##########################################################################################################
#Set up and store session users
#Adapted from https://github.com/PrettyPrinted/youtube_video_code/tree/master/2020/02/10/Creating%20a%20Login%20Page%20in%20Flask%20Using%20Sessions

class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User: {self.username}>'

users = []
users.append(User(id=1, username='admin', password='admin'))
users.append(User(id=2, username='Shane', password='password'))
users.append(User(id=3, username='Andrew', password='1234'))

###########################################################################################################
###########################################################################################################
#Flask links with login requirements

app = Flask(__name__, static_url_path='', static_folder='rnlipages')
app.secret_key = 'savinglivesatsea'

#Check for User
@app.before_request
def before_request():
    g.user = None

    if 'user_id' in session:
        user = [x for x in users if x.id == session['user_id']][0]
        g.user = user

#Login page to verify credentials and start session
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.pop('user_id', None)

        username = request.form['username']
        password = request.form['password']
        
        user = [x for x in users if x.username == username][0]
        if user and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for('profile'))

        return redirect(url_for('login'))

    return render_template('login.html')

#Session Logout page
@app.route('/logout')
def logout():
    session.clear()
    return redirect('homepage.html')

#Redirect if not looged in
@app.route('/notlogged')
def notlogged():

    return redirect('to_login.html')

#Logged in User Home page
@app.route('/profile')
def profile():
    if not g.user:
        return redirect(url_for('login'))

    return render_template('profile.html')

#Redirect to Homepage
@app.route('/')
def index():
    
    return redirect('homepage.html')

#########################################################################################
#Flask commands that link to db

@app.route('/boatsdb')
def boatsDB():
    if not g.user:
        return redirect(url_for('notlogged'))

    return redirect('boatsdb.html')

@app.route('/locationsdb')
def locationsDB():
    if not g.user:
        return redirect(url_for('notlogged'))

    return redirect('locationsdb.html')

@app.route('/boats')
def getAllBoats():
    if not g.user:
        return redirect(url_for('notlogged'))

    return jsonify(rnliDao.getAllBoats())

@app.route('/stations')
def getAllStations():
    if not g.user:
        return redirect(url_for('notlogged'))
    return jsonify(rnliDao.getAllStations())

@app.route('/boats/<int:ID>')
def findBoatById(ID):
    if not g.user:
        return redirect(url_for('notlogged'))
    return jsonify(rnliDao.findBoatById(ID))

@app.route('/stations/<int:ID>')
def findStationById(ID):
    if not g.user:
        return redirect(url_for('notlogged'))
    return jsonify(rnliDao.findStationById(ID))

#########################################################################################
#########################################################################################
#CRUD COMMANDS

#Create entries  db

#curl -X POST -d "{\"ID\":12, \"type\":\"ALB\", \"class\":\"Trent\", \"crew\":6, \"length\":14.3,\"speed\":25}" -H Content-Type:application/json http://127.0.0.1:5000/boats

@app.route('/boats', methods=['POST'])
def createBoat():
    if not g.user:
        return redirect(url_for('notlogged'))
   
    if not request.json:
        abort(400)

    boat = {
        "ID": request.json["ID"],
        "type": request.json["type"],
        "class": request.json["class"],
        "crew": request.json["crew"],
        "length": request.json["length"],
        "speed": request.json["speed"]
    }
    return jsonify(rnliDao.createBoat(boat))

#curl -X POST -d "{\"ID\":46, \"station\":\"Louisburgh\", \"location\":\"Louisburgh, Mayo\", \"type\":Atlantic 75, \"launch_method\":Slipway,\"name\":Dave the boat}" -H Content-Type:application/json http://127.0.0.1:5000/stations

@app.route('/stations', methods=['POST'])
def createStation():
    if not g.user:
        return redirect(url_for('notlogged'))

    if not request.json:
        abort(400)

    station = {
        "ID": request.json["ID"],
        "station": request.json["station"],
        "location": request.json["location"],
        "type": request.json["type"],
        "launch_method": request.json["launch_method"],
        "name": request.json["name"]
    }
    return jsonify(rnliDao.createStation(station))


#########################################################################################
#update dbs

# curl -X PUT -d "{\"type\":\"ALB\", \"class\":Severn}" -H "content-type:application/json" http://127.0.0.1:5000/boats/1

@app.route('/boats/<int:ID>', methods=['PUT'])
def updateBoats(ID):

    if not g.user:
        return redirect(url_for('notlogged'))

    foundBoat=rnliDao.findBoatById(ID)
    print (foundBoat)
    if foundBoat == {}:
        return jsonify({}), 404
    currentBoat = foundBoat
    if 'type' in request.json:
        currentBoat['type'] = request.json['type']
    if 'class' in request.json:
        currentBoat['class'] = request.json['class']
    if 'crew' in request.json:
        currentBoat['crew'] = request.json['crew']
    rnliDao.updateBoats(currentBoat)
    if 'length' in request.json:
        currentBoat['length'] = request.json['length']
    if 'speed' in request.json:
        currentBoat['speed'] = request.json['speed']

    return jsonify(currentBoat)


# curl -X PUT -d "{\"station\":\"Galway\", \"launch_method\":Carriage}" -H "content-type:application/json" http://127.0.0.1:5000/stations/1

@app.route('/stations/<int:ID>', methods=['PUT'])
def updateStations(ID):

    if not g.user:
        return redirect(url_for('notlogged'))

    foundStation=rnliDao.findStationById(ID)
    print (foundStation)
    if foundStation == {}:
        return jsonify({}), 404
    currentStation = foundStation
    if 'station' in request.json:
        currentStation['station'] = request.json['station']
    if 'location' in request.json:
        currentStation['location'] = request.json['location']
    if 'type' in request.json:
        currentStation['type'] = request.json['type']
    rnliDao.updateStations(currentStation)
    if 'launch_method' in request.json:
        currentStation['launch_method'] = request.json['launch_method']
    if 'name' in request.json:
        currentStation['name'] = request.json['name']

    return jsonify(currentStation)

#########################################################################################

#delete from db

# curl -X DELETE http://127.0.0.1:5000/boats/12

@app.route('/boats/<int:ID>', methods=['DELETE'])
def deleteBoat(ID):

    if not g.user:
        return redirect(url_for('notlogged'))

    rnliDao.deleteBoat(ID)

    return jsonify({"done": True})

# curl -X DELETE http://127.0.0.1:5000/stations/12
@app.route('/stations/<int:ID>', methods=['DELETE'])
def deleteStation(ID):

    if not g.user:
        return redirect(url_for('notlogged'))

    rnliDao.deleteStation(ID)

    return jsonify({"done": True})

#########################################################################################

@app.route('/fleet')
def Stations():
    getStations()
    return redirect('fleet.html')

@app.route('/locations')
def Fleet():
    getFleet()
    return redirect('locations.html')

#getStations()
#getFleet()

if __name__ == "__main__":
    app.run(debug=True)