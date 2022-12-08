pyGreatCircleDistance
=====================

Calculate the distance between two GPS coordinates in meters

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
from pygreatcircledistance import vincenty_formula

dist = vincenty_formula((77.1539, -120.398), (77.1804, 129.55))
print(dist)  # 2332668.5392066096 meters
```
