import csv

def AddAirportToList(row, airportlist, count):
	airport_detail = []
	airport_detail.insert(0,row['NAME'])
	airport_detail.insert(1,row['ICAO'])
	airport_detail.insert(2,row['Latitude'])
	airport_detail.insert(3,row['Longitude'])
	airportlist.append(airport_detail)

def ExtractDataFromCSV(path):
	airportlist = []
	count=0
	with open(path, newline='') as csvfile:
		records = csv.DictReader(csvfile)
		for row in records:
			AddAirportToList(row, airportlist, count)
			count+=1

	return airportlist