
import math

class Airport:
    def __init__(self,code, initLatitudeDegrees, initLatitudeMinutes, initLongitudeDegrees, initLongitudeMinutes):
        self.code = code
        self.initLatitudeDegrees = initLatitudeDegrees
        self.initLatitudeMinutes = initLatitudeMinutes
        self.initLongitudeDegrees = initLongitudeDegrees
        self.initLongitudeMinutes = initLongitudeMinutes


    def getCode(self):
        return self.code
    
    def getLatitudeDegrees(self):
        return self.initLatitudeDegrees
    def getLatitudeMinutes(self):
        return self.initLatitudeMinutes
    def getLongitudeDegrees(self):
        return self.initLongitudeDegrees
    def getLongitudeMinutes(self):
        return self.initLongitudeMinutes
    
    @staticmethod 
    def calculateDistance( a1 , a2 ):
        if a1 is None or a2 is None:
            return -1
        PI_F = 3.14159265358979
        RADIAN_FACTOR = 180.0 / PI_F
        EARTH_RADIUS  = 3963.0
        lat1  = a1.getLatitudeDegrees() + a1.getLatitudeMinutes() / 60.0
        lat1 = lat1 / RADIAN_FACTOR
        long1  = -a1.getLongitudeDegrees() + a1.getLongitudeMinutes() / 60.0
        long1 = long1 / RADIAN_FACTOR
        lat2 = a2.getLatitudeDegrees() + a2.getLatitudeMinutes() / 60.0
        lat2 = lat2 / RADIAN_FACTOR
        long2 = -a2.getLongitudeDegrees() + a2.getLongitudeMinutes() / 60.0
        long2 = long2 / RADIAN_FACTOR
        x =((math.sin(lat1) * math.sin(lat2))
			+ (math.cos(lat1)
		    * math.cos(lat2)
		    * math.cos(long2 - long1)))
        x2 = (math.sqrt(1.0 - (x * x)) / x)
        distance = (EARTH_RADIUS * math.atan(x2))
        return distance


     



