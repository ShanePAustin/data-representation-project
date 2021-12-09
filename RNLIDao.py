#MySQL queries for RNLI databases for Data Representation course
#CRUD functionality

import mysql.connector
from mysql.connector import cursor
import dbconfig as cfg

#Establish connection
class RnliDao:
        #db connection
    db=""
    def ConnectToDB(self):
        self.db = mysql.connector.connect(
            host=cfg.mysql['host'],
            user=cfg.mysql['user'],
            password=cfg.mysql['password'],
            database=cfg.mysql['database'],
            #pool_name = 'connection_pool',
            #pool_size=3
        )
        #return db

    # Get a connection from the pool
    #def getConnect(self):
        #db = mysql.connector.connect(
        #pool_name='connection_pool'
        #)
        #return db

    # Initialise DB connection pool
    def __init__(self):
        self.ConnectToDB()
        #db.close()

    def getCursor(self):
        if not self.db.is_connected():
            self.connectToDB()
        return self.db.cursor()

    #Function to create a row into boat table
    def createBoat(self, boat):
        cursor = self.db.cursor()
        sql = "insert into boats (ID, type, class, crew, length, speed) values (%s,%s,%s,%s,%s,%s)"
        values = [
            boat['ID'],
            boat['type'],
            boat['class'],
            boat['crew'],
            boat['length'],
            boat['speed']                
        ]

        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid

    #Function to create a row into stations table
    def createStation(self, station):
        cursor = self.db.cursor()
        sql = "insert into stations (ID, station, location, type, launch_method, name) values (%s,%s,%s,%s,%s,%s)"
        values = [
            station['ID'],
            station['station'],
            station['location'],
            station['type'],
            station['launch_method'],
            station['name']               
        ]

        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid

    #Fetch all data from boats and convert to dict
    def getAllBoats(self):
        cursor = self.db.cursor()
        sql = 'select * from boats'
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        #print(results)
        for result in results:
            resultAsDict = self.convertBoatToDict(result)
            returnArray.append(resultAsDict)

        return returnArray

    #Fetch all data from stations and convert to dict
    def getAllStations(self):
        cursor = self.db.cursor()
        sql = 'select * from stations'
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        #print(results)
        for result in results:
            resultAsDict = self.convertStationToDict(result)
            returnArray.append(resultAsDict)

        return returnArray

    #Find by specific ID
    def findBoatById(self, ID):
        cursor = self.db.cursor()
        sql = 'select * from boats where ID = %s'
        values = [ ID ]
        cursor.execute(sql, values)
        result = cursor.fetchone()        
        return self.convertBoatToDict(result)

    #Find by specific ID
    def findStationById(self, ID):
        cursor = self.db.cursor()
        sql = 'select * from stations where ID = %s'
        values = [ ID ]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertStationToDict(result)

    #Update rows in boat table
    def updateBoats(self, boat):
       cursor = self.db.cursor()
       sql = "update boats set type = %s, class = %s, crew = %s, length = %s, speed = %s where ID = %s"
       values = [            
            boat['type'],
            boat['class'],
            boat['crew'],
            boat['length'],
            boat['speed'],  
            boat['ID']
       ]
       cursor.execute(sql, values)
       self.db.commit()

       return boat

    #Update rows in stations table
    def updateStations(self, station):
       cursor = self.db.cursor()
       sql = "update stations set station = %s, location = %s, type = %s, launch_method = %s, name = %s where ID = %s"
       values = [
            station['station'],
            station['location'],
            station['type'],
            station['launch_method'],
            station['name'],
            station['ID'] 
       ]
       cursor.execute(sql, values)
       self.db.commit()

       return station

    #Delete entry from boats table
    def deleteBoat(self, ID):
        cursor = self.db.cursor()
        sql = 'delete from boats where ID = %s'
        values = [ID]
        cursor.execute(sql, values)
        self.db.commit()   

        return {}

    #Delete entry from stations table
    def deleteStation(self, ID):
        cursor = self.db.cursor()
        sql = 'delete from stations where ID = %s'
        values = [ID]
        cursor.execute(sql, values)
        self.db.commit()   

        return {}

    #convert to dict function
    def convertBoatToDict(self, result):
        colnames = ['ID', 'type', 'class', 'crew', 'length', 'speed']
        boat = {}

        if result:
            for i , colName in enumerate(colnames):
                value = result[i]
                boat[colName] = value

        return boat

    #convert to dict function
    def convertStationToDict(self, result):
        colnames = ['ID', 'station', 'location', 'type', 'launch_method', 'name']
        station = {}

        if result:
            for i , colName in enumerate(colnames):
                value = result[i]
                station[colName] = value
                
        return station


rnliDao = RnliDao()