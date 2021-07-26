import operator
from getdatafromcsv import ExtractDataFromCSV
from haversine import Haversine
from decimaltoDMS import LatitudeDecimaltoDMS, LongitudeDecimaltoDMS
from columnar import columnar
from simple_term_menu import TerminalMenu


terminal_menu = TerminalMenu(["original csv", "modified csv for testing"])
choice_index = terminal_menu.show()
if choice_index==0:
	path = '/home/ben/Development/LatLong/uk_airport_coords.csv'
else:
	path = '/home/ben/Development/LatLong/uk_airport_coords2.csv'

AirportList = ExtractDataFromCSV(path)

terminal_menu = TerminalMenu(["use hard coded position test data Shaftesbury, Dorset", "use hard coded position test data Sydney, Australia","enter position"])
choice_index = terminal_menu.show()
if choice_index==0:
	#Shaftesbury Lat,Long
	Slat1=51.005840
	Slon1=-2.197550
elif choice_index==1:
	#Sydney International Lat,Long
	Slat1=-33.865143
	Slon1=151.2099	
elif choice_index==2:
	while True:
	    try:
	        Slat1 = float(input("Current position Latitude: "))
	    except ValueError:
	        print("please enter in format ###.####....####")
	        continue
 
	    if Slat1 > 180.00 or Slat1 <-180.00:
	        print("max is 180 min is -180, please re-enter")
	        continue
	    else:
	        #we're ready to exit the loop.
	        break

	while True:
	    try:
	        Slon1 = float(input("Current position Longitude: "))
	    except ValueError:
	        print("please enter in format ###.####....####")
	        continue

	    if Slon1 > 180 or Slon1 < -180:
	        print("max is 180 min is -180, please re-enter")
	        continue
	    else:
	        #we're ready to exit the loop.
	        break

	#input validation needed
	#Slat1 = float(input("Current position Latitude: "))
	#Slon1 = float(input("Current position Longitude: "))

LDL=[]

terminal_menu = TerminalMenu(["miles", "kilometres"])
choice_index = terminal_menu.show()
if choice_index==0:
	DistanceUnits='miles'
elif choice_index==1:
	DistanceUnits='kilometres'

for Airport in AirportList:
	Slon2=float(Airport[3])
	Slat2=float(Airport[2])
	LD=[]
	LD.insert(0, Airport[0])
	if DistanceUnits=='miles':
		LD.insert(1,float("{:.2f}".format(Haversine([Slon1,Slat1],[Slon2,Slat2]).miles)))
	if DistanceUnits=='kilometres':
		LD.insert(1,float("{:.2f}".format(Haversine([Slon1,Slat1],[Slon2,Slat2]).km)))
	LD.insert(2,(Slat2))
	LD.insert(3,(Slon2))
	LD.insert(4,LatitudeDecimaltoDMS(Slat2))
	LD.insert(5,LongitudeDecimaltoDMS(Slon2))
	LDL.append(LD)

NearestAirports = sorted(LDL, key=operator.itemgetter(1))

nearest=[]
count=0
#NoOfResults = int(input("number of airports to display: "))

print('Enter number of airports to show')
terminal_menu = TerminalMenu(["default ", "enter number to show"])
choice_index = terminal_menu.show()
if choice_index==0:
	NoOfResults=1
elif choice_index==1:
	NoOfResults = int(input("number of airports to display: "))

for i in range(NoOfResults):
	nearest.append(NearestAirports[count])
	count = count+1

print(NoOfResults, " nearest airports to Lat:", str(Slat1),"Lon:",str(Slon1))

ColumnHeaders = ['Airport', 'Distance '+DistanceUnits, 'DD Lat', 'DD Lon', 'DMS Lat', 'DMS Lon']
table = columnar(nearest, ColumnHeaders, no_borders=False)
print(table)