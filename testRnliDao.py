from RNLIDao import rnliDao

boat1 = {
    'ID' : 1,
    'type' : 'ALB',
    'class' : 'Severn',
    'crew' : 7,
    'length' : 17.3,
    'speed' : 25, 

}

boat2 = {
    'ID' : 2,
    'type' : 'ALB',
    'class' : 'Tamar',
    'crew' : 7,
    'length' : 16.3,
    'speed' : 25, 

}

station1 = {
    'ID' : 1,
    'station' : 'Portrush',
    'location' : 'Portrush, County Antrim',
    'type' : '	Severn, D-class (IB1)',
    'launch_method' : 'Moored afloat, Slipway',
    'name' : 'William Gordon Burr (ON 1257), David Roulston (Civil Service No. 52) (D-738)', 

}

#returnValue = rnliDao.create(boat2)
#returnValue = rnliDao.getAll()
#print(returnValue)
returnValue = rnliDao.createStation(station1)
returnValue = rnliDao.getAllStations()
print(returnValue)
#returnValue = boatDao.findById(boat2['id'])
#print('find By ID')
#print(returnValue)
#returnValue = boatDao.update(boat2)
#print(returnValue)
#returnValue = boatDao.findById(boat2['ISBN'])
#print(returnValue)
#returnValue = boatDao.delete(boat2['ISBN'])
#print(returnValue)
#returnValue = boatDao.getAll()
#print(returnValue)