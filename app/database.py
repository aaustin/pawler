from app import db

class Sensor(db.Model):
	row_id = db.Column(db.Integer, unique = True, primary_key = True)
	device_id = db.Column(db.Integer, index = True)
	time = db.Column(db.Integer)
	temp = db.Column(db.Float)
	accX = db.Column(db.Float)
	accY = db.Column(db.Float)
	accZ = db.Column(db.Float)

	def __init__(self, device_id, temp, time, accX, accY, accZ):
		self.device_id = device_id
		self.time = time
		self.temp = temp
		self.accX = accX
		self.accY = accY
		self.accZ = accZ

	def __repr__(self):
		return '<row_id: %r>' % self.row_id
