import sheetupdate
import datetime
from random import randint
from time import sleep
from sense_hat import SenseHat

def testsheet():
	spreadsheetId = "1VleCxOoz7hOAvUF_jgTIji79Tebg09jXjPGSqp2oU84"
	rangeName = 'A1:D'
	values = {"values":[["Time", "Temperature", "pressure", "Humidity"],]}
	sheetupdate.update_authenticate(spreadsheetId, rangeName, values)
	sense = SenseHat()
	try:
		while True:
			for i in range(2,999):
				myTS = "{:%H:%M:%S}".format(datetime.datetime.now())
				t=round(sense.get_temperature(),2)
				p=round(sense.get_pressure(),2)
				h=round(sense.get_humidity(),2)
				values = {"values":[[myTS,t,p,h],]}
				rangeName = 'A' +str(i) + ':D'
				sheetupdate.update_authenticate(spreadsheetId, rangeName, values)
				sleep(5)
	except KeyboardInterrupt:
		pass
if __name__ == '__main__':
	testsheet()
