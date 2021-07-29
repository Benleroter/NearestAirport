'''function to convert decimal co-ordinates into degree, minute, second format'''
'''negative latitudes represent the southern hemisphere, and negative longitudes represent the western hemisphere'''

def DecimaltoDMS(coordinate, lat_or_long):
    d = int(coordinate)
    m = int((coordinate - d) * 60)
    s= round((coordinate - d - m/60) * 3600.00, 2)
    
    DMS=str(abs(0))+"º "+str(abs(0))+"' "+str(abs(0.00))+'" '+"bad"
    
    if lat_or_long == 0 and d >= 0:
        DMS=str(abs(d))+"º "+str(abs(m))+"' "+str(abs(s))+'" '+"N"
    elif lat_or_long == 0:
        DMS=str(abs(d))+"º "+str(abs(m))+"' "+str(abs(s))+'" '+"S"

    if lat_or_long == 1 and d >= 0:
        DMS=str(abs(d))+"º "+str(abs(m))+"' "+str(abs(s))+'" '+"E"
    elif lat_or_long == 0:
        DMS=str(abs(d))+"º "+str(abs(m))+"' "+str(abs(s))+'" '+"W"

    return DMS

