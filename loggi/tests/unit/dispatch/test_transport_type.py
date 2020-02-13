import pytest

from dispatch.transport_type import TransportType, get_max_checkin_geofence_distance

@pytest.mark.parametrize('tt, dist', [
        (TransportType.Motorcycle, 600),
        (TransportType.Van, 1500),
        (TransportType.Car, 743.59),
        (TransportType.Others, 743.59),
        (TransportType.Invalid, 743.59)
])
def test_dist(tt, dist):
    assert get_max_checkin_geofence_distance(tt) == dist
