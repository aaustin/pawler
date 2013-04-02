from app import app, definitions
from forms import UploadCollarData
from flask import render_template, request, jsonify

@app.route('/')
@app.route('/index')
def index():
    user = { 'nickname': 'Mada' } # fake user
    return render_template("index.html",
        title = 'Home',
        user = user)
		
@app.route('/collar/upload', methods=['POST'])
def handle_upload_view():
	return definitions.handle_upload()

@app.route('/post', methods = ['POST'])
def post():
	if request.method == 'POST':
		data = {'method' : request.method, 'stuff' : request.form['device_id']}
		resp = jsonify(data)
		resp.status_code = 200
		return resp

	'''
@app.route('/upload', methods = ['GET','POST'])
def upload():
	form = UploadCollarData()
	if form.validate_on_submit():
		device_id = form.device_id.data
		time = form.time.data
		temp = form.temp.data
		accX = form.accX.data
		accY = form.accY.data
		accZ = form.accZ.data
		data = open('pawler/app/data/data.txt','a')
		str = "%i %i %f %f %f %f" %(device_id, time, temp, accX, accY, accZ)
		data.write(str)
		data.close()
	return render_template('upload.html', title = 'home')
	 '''
		

		


