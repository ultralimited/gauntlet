from flask import Flask, render_template, request, redirect, url_for, make_response
import press3
# import RPi.GPIO as GPIO

#GPIO.setmode(GPIO.BCM) #set up GPIO

app = Flask(__name__) #set up flask server

#when the root IP is selected, return index.html page
@app.route('/')
def index():

	return render_template('index.html')

#recieve which pin to change from the button press on index.html
#each button returns a number that triggers a command in this function
#
#Uses methods from motors.py to send commands to the GPIO to operate the motors
@app.route('/<action>', methods=['POST'])
def reroute(action):

	action = int(action)
	heads = []
	heads.append(request.form.get('H1') == 'on')
	heads.append(request.form.get('H2') == 'on')
	heads.append(request.form.get('H3') == 'on')
	heads.append(request.form.get('H4') == 'on')
	heads.append(request.form.get('H5') == 'on')
	heads.append(request.form.get('H6') == 'on')
	heads.append(request.form.get('H7') == 'on')
	heads.append(request.form.get('H8') == 'on')

	double = []
	double.append(request.form.get('D1') == 'on')
	double.append(request.form.get('D2') == 'on')
	double.append(request.form.get('D3') == 'on')
	double.append(request.form.get('D4') == 'on')
	double.append(request.form.get('D5') == 'on')
	double.append(request.form.get('D6') == 'on')
	double.append(request.form.get('D7') == 'on')
	double.append(request.form.get('D8') == 'on')

	rotateCount = request.form.get('R');
	loopCount = request.form.get('L');
	dwell = request.form.get('DWELL');

	if action == 100:
		press3.tableUp()
	elif action == 200:
		press3.tableDown()
	elif action == 300:
		press3.go()
	elif action == 400:
		press3.printHeads(heads, double)
	elif action == 500:
		press3.printHeadsTest(heads)
	elif action == 600:
		press3.rotate(rotateCount)
	elif action == 700:
		print("ACTION 700")
		press3.printInLoop(loopCount, heads, double, dwell)
	response = make_response(redirect(url_for('index')))
	return(response)

app.run(debug=True, host='0.0.0.0', port=8000) #set up the server in debug mode to the port 8000

