from simple_term_menu import TerminalMenu

terminal_menu = TerminalMenu(["use hard coded position test data Shaftesbury, Dorset", "use hard coded position test data Alice Springs, Australia","enter position"])
choice_index = terminal_menu.show()
if choice_index==0:
	#Shaftesbury Lat,Long
	Slat1=51.005840
	Slon1=-2.197550
elif choice_index==1:
	#Alice Springs International Lat,Long
	Slat1=-23.698042
	Slon1=133.880753
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
	        #we're ready to exit the loop.
	        break

print('Slon1',Slon1)