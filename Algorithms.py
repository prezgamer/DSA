from math import radians, cos, sin, asin, sqrt

"""
Calculate the great circle distance in kilometers between two points 
on the earth (specified in decimal degrees)
"""
def Haversine(lon1, lat1, lon2, lat2):
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles. Determines return value units.
    return c * r


def Dijkstra():
    pass


# CEK to OVB
# CEKLat = 55.305801
# CEKLon = 61.5033
# OVBLat = 55.012599945068
# OVBLon = 82.650703430176
# dist = haversine(CEKLon, CEKLat, OVBLon, OVBLat)
# print(dist)