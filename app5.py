from flask import Flask, render_template, request, redirect, url_for, make_response
import press5 as press
# GIT VERSION
app = Flask(__name__)  # set up flask server


@app.route('/')
def index():
    return render_template('index5.html')


@app.route('/callfunction', methods=['POST'])
def callfunction():
    headsData = request.form['heads']
    secondHitData = request.form['double']
    loopCount = int(request.form['loopCount'])
    dwellTime = int(request.form['dwellTime'])
    hoodyEnabled = request.form['hoodyEnabled'] == 'true'

    print(hoodyEnabled)

    heads = []
    secondHit = []

    for x in headsData:
        heads.append(x == '1')

    for x in secondHitData:
        secondHit.append(x == '1')

    action = request.form['action']
    if action == 'tableUp':
        press.tableUp()
    elif action == 'tableDown':
        press.tableDown()
    elif action == 'printOnce':
        press.printOnce(heads, secondHit, hoodyEnabled)
    elif action == "printAuto":
        press.printAuto(heads, secondHit, loopCount, dwellTime, hoodyEnabled)
    elif action == 'printClean':
        press.printClean(heads, secondHit)
    return index()


# set up the server in debug mode to the port 8000
app.run(debug=True, host='0.0.0.0', port=8000)
