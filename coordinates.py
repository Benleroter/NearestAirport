


def DataEntryAndValidation():
	position=[]
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
	        break

	position.append(Slat1) 
	print('Slat1',Slat1)

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
	        break

	position.append(Slon1) 
	print('Slon1',Slon1)

	return position