from pygreatcircledistance import (
    _coords_to_radians,
    haversine_formula,
    spherical_law_of_cosines_formula,
    vincenty_formula,
)

_FROM_COORDS = (77.1539, -120.398)
_TO_COORDS = (77.1804, 129.55)


def test_coords_to_radians() -> None:
    output = tuple(round(num, 6) for num in _coords_to_radians(_FROM_COORDS))
    assert output == (1.34659, -2.101342), output


def test_haversine_formula() -> None:
    distance = haversine_formula(_FROM_COORDS, _TO_COORDS)
    assert round(distance, 3) == 2332668.539, distance


def test_spherical_law_of_cosines_formula() -> None:
    distance = spherical_law_of_cosines_formula(_FROM_COORDS, _TO_COORDS)
    assert round(distance, 3) == 2332668.539, distance


def test_vincenty_formula() -> None:
    distance = vincenty_formula(_FROM_COORDS, _TO_COORDS)
    assert round(distance, 3) == 2332668.539, distance
