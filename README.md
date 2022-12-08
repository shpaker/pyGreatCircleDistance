pyGreatCircleDistance
=====================

Calculate the distance between two GPS coordinates in meters

[![PyPI](https://img.shields.io/pypi/v/pyGreatCircleDistance.svg)](https://pypi.python.org/pypi/pyGreatCircleDistance)
[![PyPI](https://img.shields.io/pypi/dm/pyGreatCircleDistance.svg)](https://pypi.python.org/pypi/pyGreatCircleDistance)
[![Docker Pulls](https://img.shields.io/docker/pulls/shpaker/pyGreatCircleDistance)](https://hub.docker.com/r/shpaker/pyGreatCircleDistance)
[![PyPI](https://img.shields.io/badge/code%20style-black-000000.svg)](href="https://github.com/psf/black)

Installation
------------

```
pip install pyGreatCircleDistance -U
```

Example
-------

```
>>> from_coords = (77.1539, -120.398)
>>> to_coords = (77.1804, 129.55)
>>> dist = calc_distance(from_coords, to_coords)
>>> print(dist)
2332668.5392066096
```
