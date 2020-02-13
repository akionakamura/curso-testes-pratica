from enum import Enum

class TransportType(Enum):
    Invalid = 0
    Motorcycle = 1
    Van = 2
    Car = 3
    Others = 4

DEFAULT_MIN_CHECKIN_DIST = 743.59
MIN_CHECKIN_DIST = {
    TransportType.Motorcycle: 600,
    TransportType.Van: 1500
}

def get_max_checkin_geofence_distance(transport_type):
    return MIN_CHECKIN_DIST.get(transport_type, DEFAULT_MIN_CHECKIN_DIST)
