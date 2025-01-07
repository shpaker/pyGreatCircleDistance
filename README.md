pyGreatCircleDistance
=====================

A Python package to calculate the distance between two GPS coordinates in meters. 

[![PyPI](https://img.shields.io/pypi/v/pyGreatCircleDistance.svg)](https://pypi.python.org/pypi/pyGreatCircleDistance)
[![PyPI](https://img.shields.io/pypi/dm/pyGreatCircleDistance.svg)](https://pypi.python.org/pypi/pyGreatCircleDistance)
[![PyPI](https://img.shields.io/badge/code%20style-black-000000.svg)](href="https://github.com/psf/black)

Installation
------------

```
pip install pyGreatCircleDistance -U
```

Example
-------

```python
from pygreatcircledistance import haversine_formula, spherical_law_of_cosines_formula, vincenty_formula

from_coords = (77.1539, -120.398)
to_coords = (77.1804, 129.55)

# Haversine formula: simpler and faster but less accurate for long distances and near the poles. Assumes a perfect sphere.
dist_haversine = haversine_formula(from_coords, to_coords)
print(f"Haversine formula distance: {dist_haversine} meters")

# Spherical Law of Cosines formula: more accurate than the Haversine formula for long distances but still assumes a perfect sphere.
dist_spherical_cosines = spherical_law_of_cosines_formula(from_coords, to_coords)
print(f"Spherical Law of Cosines formula distance: {dist_spherical_cosines} meters")

# Vincenty formula: the most accurate as it takes into account the ellipsoidal shape of the Earth. More computationally intensive.
dist_vincenty = vincenty_formula(from_coords, to_coords)
print(f"Vincenty formula distance: {dist_vincenty} meters")
```
