from flask.ext.wtf import Form, IntegerField, FloatField 
from flask.ext.wtf import Required

class UploadCollarData(Form):
	device_id = IntegerField('device_id')
	time = IntegerField('time')
	temp = FloatField('temp')
	accX = FloatField('accX', validators = [Required()])
	accY = FloatField('accY', validators = [Required()])
	accZ = FloatField('accZ', validators = [Required()])
