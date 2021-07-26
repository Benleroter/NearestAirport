import operator
from getdatafromcsv import ExtractDataFromCSV
from haversine import Haversine
from decimaltoDMS import LatitudeDecimaltoDMS, LongitudeDecimaltoDMS
from columnar import columnar
from simple_term_menu import TerminalMenu
from coordinates import DataEntryAndValidation


print('Choose base airport data')
path_menu = TerminalMenu(["UK airports csv", "Worldwide airports csv for testing"])
path_index = path_menu.show()
if path_index==0:
	path = '/home/ben/Development/LatLong/uk_airport_coords.csv'
else:
	path = '/home/ben/Development/LatLong/world_airport_coords.csv'

AirportList = ExtractDataFromCSV(path)

print('Choose pre-defined position or enter co-ordinates ')
input_menu = TerminalMenu(["test data Shaftesbury, Dorset", "test data Alice Springs, Australia","enter position"])
input_index = input_menu.show()
if input_index==0:
	#Shaftesbury Lat,Long
	Slat1=51.005840
	Slon1=-2.197550
	print('[INFO] Co-ordinates chosen-Shaftesbury:', Slat1,", ",Slon1)	
elif input_index==1:
	#Alice Springs International Lat,Long
	Slat1=-23.698042
	Slon1=133.880753
	print('[INFO] Co-ordinates chosen-Alice Springs:', Slat1,", ",Slon1)	
elif input_index==2:
	Pos=[]
	Pos=DataEntryAndValidation() 
	Slat1 = Pos[0]
	Slon1 = Pos[1]
	print('[INFO] Co-ordinates chosen:', Slat1,", ", Slon1)	

AirportAndDistanceList=[]

print('Choose output units')
terminal_menu = TerminalMenu(["miles", "kilometres"])
choice_index = terminal_menu.show()
if choice_index==0:
	DistanceUnits='miles'
elif choice_index==1:
	DistanceUnits='kilometres'

print('[INFO] Units chosen:', DistanceUnits )	

for Airport in AirportList:
	Slon2=float(Airport[3])
	Slat2=float(Airport[2])
	AirportAndDistance=[]
	AirportAndDistance.insert(0, Airport[0])
	if DistanceUnits=='miles':
		AirportAndDistance.insert(1,float("{:.2f}".format(Haversine([Slon1,Slat1],[Slon2,Slat2]).miles)))
	if DistanceUnits=='kilometres':
		AirportAndDistance.insert(1,float("{:.2f}".format(Haversine([Slon1,Slat1],[Slon2,Slat2]).km)))
	AirportAndDistance.insert(2,(Slat2))
	AirportAndDistance.insert(3,(Slon2))
	AirportAndDistance.insert(4,LatitudeDecimaltoDMS(Slat2))
	AirportAndDistance.insert(5,LongitudeDecimaltoDMS(Slon2))
	AirportAndDistanceList.append(AirportAndDistance)

NearestAirports = sorted(AirportAndDistanceList, key=operator.itemgetter(1))

print('Enter number of airports to show')
terminal_menu = TerminalMenu(["default (1)", "enter number to show", "All"])
choice_index = terminal_menu.show()
if choice_index==0:
	NoOfResults=1
elif choice_index==1:
	NoOfResults = int(input("number of airports to display: "))
elif choice_index==2:
	NoOfResults=len(NearestAirports)

nearest=[]
count=0
for i in range(NoOfResults):
	nearest.append(NearestAirports[count])
	count = count+1

print(NoOfResults, " nearest airports to Lat:", str(Slat1),"Lon:",str(Slon1))

ColumnHeaders = ['Airport', 'Distance '+DistanceUnits, 'DD Lat', 'DD Lon', 'DMS Lat', 'DMS Lon']
table = columnar(nearest, ColumnHeaders, no_borders=False)
print(table)