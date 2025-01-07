from __future__ import annotations

from math import pow  # pylint: disable=redefined-builtin
from math import acos, asin, atan2, cos, radians, sin, sqrt
from typing import Tuple

__all__ = (
    "spherical_law_of_cosines_formula",
    "haversine_formula",
    "vincenty_formula",
)
__version__ = "0.1.0"

_EARTH_RADIUS = 6372795  # meters


def _coords_to_radians(
    coords: Tuple[float, float],
) -> Tuple[float, float]:
    """
    Convert coordinates from degrees to radians.

    Args:
        coords (Tuple[float, float]): A tuple containing latitude and longitude in degrees.

    Returns:
        Tuple[float, float]: A tuple containing latitude and longitude in radians.
    """
    return radians(coords[0]), radians(coords[1])


def haversine_formula(
    from_coords: Tuple[float, float],
    to_coords: Tuple[float, float],
) -> float:
    """
    Calculate the great-circle distance between two points on the Earth's surface using the Haversine formula.
    
    The Haversine formula is an equation that can be used to find the distance between two points on the surface of a sphere given their longitudes and latitudes.
    More information: https://en.wikipedia.org/wiki/Haversine_formula

    Args:
        from_coords (Tuple[float, float]): A tuple containing the latitude and longitude of the starting point in degrees.
        to_coords (Tuple[float, float]): A tuple containing the latitude and longitude of the destination point in degrees.

    Returns:
        float: The distance between the two points in meters.
    """
    from_radians = _coords_to_radians(from_coords)
    to_radians = _coords_to_radians(to_coords)

    delta_longitudes = to_radians[1] - from_radians[1]

    angle_degrees = 2 * asin(
        sqrt(
            pow(sin((to_radians[0] - from_radians[0]) / 2), 2)
            + cos(from_radians[0])
            * cos(to_radians[0])
            * pow(sin(delta_longitudes / 2), 2)
        )
    )

    return angle_degrees * _EARTH_RADIUS


def spherical_law_of_cosines_formula(
    from_coords: Tuple[float, float],
    to_coords: Tuple[float, float],
) -> float:
    """
    Calculate the great-circle distance between two points on the Earth's surface using the Spherical Law of Cosines formula.
    
    The Spherical Law of Cosines is a theorem in spherical trigonometry that relates the sides and angles of spherical triangles.
    More information: https://en.wikipedia.org/wiki/Spherical_law_of_cosines

    Args:
        from_coords (Tuple[float, float]): A tuple containing the latitude and longitude of the starting point in degrees.
        to_coords (Tuple[float, float]): A tuple containing the latitude and longitude of the destination point in degrees.

    Returns:
        float: The distance between the two points in meters.
    """
    from_radians = _coords_to_radians(from_coords)
    to_radians = _coords_to_radians(to_coords)

    cos_latitudes = [cos(from_radians[0]), cos(to_radians[0])]
    sin_latitudes = [sin(from_radians[0]), sin(to_radians[0])]
    delta_longitudes = to_radians[1] - from_radians[1]

    angle_degrees = acos(
        sin_latitudes[0] * sin_latitudes[1]
        + cos_latitudes[0] * cos_latitudes[1] * cos(delta_longitudes)
    )

    return angle_degrees * _EARTH_RADIUS


def vincenty_formula(
    from_coords: Tuple[float, float],
    to_coords: Tuple[float, float],
) -> float:
    """
    Calculate the great-circle distance between two points on the Earth's surface using Vincenty's formula.
    
    Vincenty's formulae are two related iterative methods used in geodesy to calculate the distance between two points on the surface of a spheroid.
    More information: https://en.wikipedia.org/wiki/Vincenty%27s_formulae

    Args:
        from_coords (Tuple[float, float]): A tuple containing the latitude and longitude of the starting point in degrees.
        to_coords (Tuple[float, float]): A tuple containing the latitude and longitude of the destination point in degrees.

    Returns:
        float: The distance between the two points in meters.
    """
    from_radians = _coords_to_radians(from_coords)
    to_radians = _coords_to_radians(to_coords)

    cos_latitudes = [cos(from_radians[0]), cos(to_radians[0])]
    sin_latitudes = [sin(from_radians[0]), sin(to_radians[0])]
    delta_longitudes = to_radians[1] - from_radians[1]

    numerator = sqrt(
        pow(cos_latitudes[1] * sin(delta_longitudes), 2)
        + pow(
            cos_latitudes[0] * sin_latitudes[1]
            - sin_latitudes[0] * cos_latitudes[1] * cos(delta_longitudes),
            2,
        )
    )
    denominator = sin_latitudes[0] * sin_latitudes[1] + cos_latitudes[
        0
    ] * cos_latitudes[1] * cos(delta_longitudes)

    angle_degrees = atan2(numerator, denominator)

    return angle_degrees * _EARTH_RADIUS
