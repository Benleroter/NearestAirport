

class DataEntryAndValidation():
	"""Prompts user to enter co-ordinates and then validates inpiut is a float then checks values are between 180 and -180"""
	def GetCoordinate(self, lat_or_long):	

		if lat_or_long=='Lat':
			prompttext = "Current position Latitude: "
	
		elif lat_or_long=='Lon':
			prompttext = "Current position Longitude: "

		while True:
		    try:
		        coordinate = float(input(prompttext))
		    except ValueError:
		        print("please enter in format ###.####....####")
		        continue
	 
		    if coordinate > 180.00 or coordinate <-180.00:
		        print("max is 180 min is -180, please re-enter")
		        continue
		    else:
		        break
		self.coordinate = coordinate