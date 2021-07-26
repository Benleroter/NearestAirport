'''
Main program, calls units and functions to load data from csv file, prompts users to choose data set, 
distance units, number of results to display. Uses the Haversine formula to calculate the arc bewtween two pionts
on the globe. Displays latitude and longittude in both DD and DMS formats.

Two datasets (csv's), one as supplied and another where I added locations around the world for test purposes. For testing 
purposes there ar two locations hard coded, one in England and the other in Australia   
'''

import operator
from getdatafromcsv import ExtractDataFromCSV
from haversine import Haversine
from decimaltoDMS import LatitudeDecimaltoDMS, LongitudeDecimaltoDMS
from columnar import columnar
from simple_term_menu import TerminalMenu
from coordinate_entry import DataEntryAndValidation


print('Choose base airport data')
path_menu = TerminalMenu(["UK airports csv", "Worldwide airports csv for testing"])
path_index = path_menu.show()
if path_index==0:
	path = '/home/ben/Development/LatLong/uk_airport_coords.csv'
else:
	path = '/home/ben/Development/LatLong/world_airport_coords.csv'

airport_list = ExtractDataFromCSV(path)

print('Choose pre-defined position or enter co-ordinates ')
input_menu = TerminalMenu(["test data Shaftesbury, Dorset", "test data Alice Springs, Australia","enter position"])
input_index = input_menu.show()
if input_index==0:
	#Shaftesbury Lat,Long
	latitude1 = 51.005840
	longitude1 = -2.197550
	print('[INFO] Co-ordinates chosen-Shaftesbury:', latitude1,", ",longitude1)	

elif input_index==1:
	#Alice Springs International Lat,Long
	latitude1 = -23.698042
	longitude1 = 133.880753
	print('[INFO] Co-ordinates chosen-Alice Springs:', latitude1,", ",longitude1)	

elif input_index==2:
	#user prompted for co-ordinates
	Lat = DataEntryAndValidation() 
	Lat.GetCoordinate('Lat')
	Lon = DataEntryAndValidation()
	Lon.GetCoordinate('Lon')

	latitude1 = Lat.coordinate
	longitude1 = Lon.coordinate

	print('[INFO] Co-ordinates chosen:', latitude1,", ", longitude1)	

airport_and_distance_list=[]

print('Choose output units')
terminal_menu = TerminalMenu(["miles", "kilometres"])
choice_index = terminal_menu.show()
if choice_index==0:
	distance_units = 'miles'

elif choice_index==1:
	distance_units = 'kilometres'

print('[INFO] Units chosen:', distance_units )	

for Airport in airport_list:
	Lon2 = float(Airport[3])
	Lat2 = float(Airport[2])
	airport_and_distance_attributes=[]
	airport_and_distance_attributes.insert(0, Airport[0])
	if distance_units=='miles':
		airport_and_distance_attributes.insert(1,float("{:.2f}".format(Haversine([longitude1,latitude1],[Lon2,Lat2]).miles)))
	if distance_units=='kilometres':
		airport_and_distance_attributes.insert(1,float("{:.2f}".format(Haversine([longitude1,latitude1],[Lon2,Lat2]).km)))
	airport_and_distance_attributes.insert(2,(Lat2))
	airport_and_distance_attributes.insert(3,(Lon2))
	airport_and_distance_attributes.insert(4,LatitudeDecimaltoDMS(Lat2))
	airport_and_distance_attributes.insert(5,LongitudeDecimaltoDMS(Lon2))
	airport_and_distance_list.append(airport_and_distance_attributes)

nearest_airports = sorted(airport_and_distance_list, key=operator.itemgetter(1))

print('Enter number of airports to show')
terminal_menu = TerminalMenu(["default (1)", "enter number to show", "All"])
choice_index = terminal_menu.show()
if choice_index==0:
	no_of_results = 1
elif choice_index==1:
	no_of_results = int(input("number of airports to display: "))
elif choice_index==2:
	no_of_results = len(nearest_airports)

nearest = []
count = 0
for i in range(no_of_results):
	nearest.append(nearest_airports[count])
	count = count+1

print(no_of_results, " nearest airports to Lat:", str(latitude1),"Lon:",str(longitude1))

ColumnHeaders = ['Airport', 'Distance '+distance_units, 'DD Lat', 'DD Lon', 'DMS Lat', 'DMS Lon']
table = columnar(nearest, ColumnHeaders, no_borders=False)
print(table)