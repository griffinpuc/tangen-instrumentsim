"""Mock Instrument Flask Instance

Usage:
  flaskApp.py -p <port>

Options:
  -p --port     Specify a custom port (necessary for multiple instruments)

"""
from flask import Flask, send_file, jsonify, url_for
from docopt import docopt
import random
import socket
import json
import io

def startServerThread(instrumentAddress, instrumentPort):

    app = Flask(__name__)
    
    @app.route("/tdx/getInstrumentStatus")
    def status():
        return jsonify(json.load(open("json/instrumentStatus.json"))), 200

    @app.route("/tdx/getResults")
    def testlist():
        data = json.loads(open("json/RESULTS.json").read())
        newUniqueID = str(random.randint(1,99999))
        newResult = {'sampleID': newUniqueID, 'dateTime': '06-Feb-19 2:48:17 PM', 'uniqueID': newUniqueID}

        return jsonify(json.load(open("json/RESULTS.json"))), 200

    @app.route("/tdx/getTestResult/<uniqueID>")
    def dataresult(uniqueID):
        return jsonify(json.load(open("json/DATA-" + uniqueID + ".json"))), 200

    @app.route("/tdx/getRawResult")
    def rawresult():
        with open("json/resultRaw.brd", 'rb') as bites:
            return send_file(
                    io.BytesIO(bites.read()),
                    attachment_filename='test.brd',
                    mimetype='application/octet-stream')

    app.run(host=instrumentAddress, port=instrumentPort)

instrumentAddress = socket.gethostbyname(socket.gethostname())
startServerThread(instrumentAddress, 5000)