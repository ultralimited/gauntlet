from flask import Flask, render_template, request, redirect, url_for, make_response
import press2
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
	
	if action == 100:
		press21.tableUp()
	elif action == 200:
		press21.tableDown()
	elif action == 300:
		press21.go()
	elif action == 400:
		press21.printHeads(heads)
	elif action == 500:
		press21.printHeadsTest(heads)
		
	response = make_response(redirect(url_for('index')))
	return(response)

app.run(debug=True, host='0.0.0.0', port=8000) #set up the server in debug mode to the port 8000

