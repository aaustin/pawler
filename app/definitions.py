from flask import request, jsonify
from database import db, Sensor

def handle_upload():
	# grab the data from the form
	device_id = int(request.form['device_id'])
	time = int(request.form['time'])
	temp = float(request.form['temp'])
	accX = float(request.form['acc_x'])
	accY = float(request.form['acc_y'])
	accZ = float(request.form['acc_z'])

	# create a new table row
	new_sensor_data = Sensor(
			device_id=request.form['device_id'],
			time=request.form['time'],
			temp=request.form['temp'],
			accX=request.form['acc_x'],
			accY=request.form['acc_y'],
			accZ=request.form['acc_z'])
		
	# upload the row to the database
	db.session.add(new_sensor_data)	
	db.session.commit()

	# write to text file
	new_text_data = open('app/data/data.txt','a')
	str = "%i %i %f %f %f %f" %(device_id, time, temp, accX, accY, accZ)
	new_text_data.write(str)
	new_text_data.close()
	
	data = {
        'message'  : 'success',
		'status' : 'uploaded'
    }
	resp = jsonify(data)
	resp.status_code = 200
	return resp
