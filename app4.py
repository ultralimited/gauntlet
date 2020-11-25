from flask import Flask, render_template, request, redirect, url_for, make_response
import press4 as press
# GIT VERSION
app = Flask(__name__)  # set up flask server

@app.route('/')
def index():
    return render_template('index4.html')


@app.route('/callfunction', methods=['POST'])
def callfunction():
    headsData = request.form['heads']
    secondHitData = request.form['double']

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
    elif action == 'prePrint':
        press.prePrint()
    elif action == 'flood':
        press.flood(heads)
    elif action == 'rotate':
        press.rotate()
    elif action == 'print':
        press.doPrint(heads)
    elif action == 'secondFlood':
        press.flood(secondHit)
    elif action == 'secondHit':
        press.doPrint(secondHit)
    elif action == 'dwell':
        press.dwell(int(request.form['dwellTime']))
    return index()


# set up the server in debug mode to the port 8000
app.run(debug=True, host='0.0.0.0', port=8000)
