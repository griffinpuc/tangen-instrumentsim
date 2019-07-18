"""Mock Instrument Flask Instance

Usage:
  flaskApp.py -p <port>

Options:
  -p --port     Specify a custom port (necessary for multiple instruments)

"""
#Dependencies
from flask import Flask, send_file, jsonify, url_for
from docopt import docopt
import random
import socket
import json
import io

#Flask server
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


#Main argument handler
if __name__ == '__main__':
    arguments = docopt(__doc__, version='MTISIM 0.0.2')


if((arguments['<port>'] != None)):
    instrumentAddress = socket.gethostbyname(socket.gethostname())
    instrumentPort = arguments['<port>']

    print(("Instrument address: {0}:{1}").format(instrumentAddress, instrumentPort))
    startServerThread(instrumentAddress, instrumentPort)
else:
    print("No port specifed, exiting launch.")