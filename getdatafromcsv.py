import csv

def AddAirportToList(row, airportlist, count):
	airportdetail = []
	airportdetail.insert(0,row['NAME'])
	airportdetail.insert(1,row['ICAO'])
	airportdetail.insert(2,row['Latitude'])
	airportdetail.insert(3,row['Longitude'])
	airportlist.append(airportdetail)

def ExtractDataFromCSV(path):
	airportlist = []
	count=0
	with open(path, newline='') as csvfile:
		records = csv.DictReader(csvfile)
		for row in records:
			AddAirportToList(row, airportlist, count)
			count+=1

	return airportlist