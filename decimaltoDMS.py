

def LatitudeDecimaltoDMS(coordinate):
    d = int(coordinate)
    m = int((coordinate - d) * 60)
    s= round((coordinate - d - m/60) * 3600.00, 2)

    if d >= 0:
        DMS=str(abs(d))+"º "+str(abs(m))+"' "+str(abs(s))+'" '+"N"
    else:
        DMS=str(abs(d))+"º "+str(abs(m))+"' "+str(abs(s))+'" '+"S"

    return DMS

def LongitudeDecimaltoDMS(coordinate):
    d = int(coordinate)
    m = int((coordinate - d) * 60)
    s= round((coordinate - d - m/60) * 3600.00, 2)

    if d >= 0:
        DMS=str(abs(d))+"º "+str(abs(m))+"' "+str(abs(s))+'" '+"E"
    else:
        DMS=str(abs(d))+"º "+str(abs(m))+"' "+str(abs(s))+'" '+"W"
    
    return DMS