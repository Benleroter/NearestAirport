def LatitudeDecimaltoDMS(Decimal):
    d = int(Decimal)
    m = int((Decimal - d) * 60)
    s = (Decimal - d - m/60) * 3600.00
    z= round(s, 2)
    if d >= 0:
        DMS=str(abs(d))+"º "+str(abs(m))+"'"+str(abs(z))+'"'+"N"
        #print('DMS-Lat',DMS)
        #print(str(abs(d))+"º "+str(abs(m))+"\'' "+str(abs(z))+'" '+"N")
    else:
        DMS=str(abs(d))+"º "+str(abs(m))+"' "+str(abs(z))+'" '+"S"
        #print('DMS-long',DMS)
        #print(str(abs(d))+"º "+str(abs(m))+"' "+str(abs(z))+'" '+"S")

    return DMS

def LongitudeDecimaltoDMS(Decimal):
    d = int(Decimal)
    m = int((Decimal - d) * 60)
    s = (Decimal - d - m/60) * 3600.00
    z= round(s, 2)
    if d >= 0:
        DMS=str(abs(d))+"º "+str(abs(m))+"'"+str(abs(z))+'"'+"E"
        #print('DMS-Lat',DMS)
        #print(str(abs(d))+"º "+str(abs(m))+"\'' "+str(abs(z))+'" '+"E")
    else:
        DMS=str(abs(d))+"º "+str(abs(m))+"' "+str(abs(z))+'" '+"W"
        #print('DMS-long',DMS)
        #print(str(abs(d))+"º "+str(abs(m))+"' "+str(abs(z))+'" '+"W")

    return DMS