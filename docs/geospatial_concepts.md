# Geospatial Concepts

## Latitude

When looking at a map, latitude lines run horizontally.
Latitude lines are also known as parallels since they are parallel and are an equal distant from each other.
Each degree of latitude is approximately 69 miles (111 km) apart; there is a variation due to the fact that the earth is not a perfect sphere but an oblate ellipsoid (slightly egg-shaped).
To remember latitude, imagine them as the horizontal rungs of a ladder ("ladder-tude").
Degrees latitude are numbered from 0° to 90° north and south.
Zero degrees is the equator, the imaginary line which divides our planet into the northern and southern hemispheres.
90° north is the North Pole and 90° south is the South Pole.

## Longitude

The vertical longitude lines are also known as meridians.
They converge at the poles and are widest at the equator (about 69 miles or 111 km apart).
Zero degrees longitude is located at Greenwich, England (0°).
The degrees continue 180° east and 180° west where they meet and form the International Date Line in the Pacific Ocean.
Greenwich, the site of the British Royal Greenwich Observatory, was established as the site of the prime meridian by an international conference in 1884.

## Summary

Latitude (parallels) [horizontal rings eg. "ladder-tude"]
Longitude (meridians) [vertical lines]

### Which is X, which is Y?

In ESRI, Lat = Y Long = X

It's easy to get backwards.
On a standard north facing map, latitude is represented by horizontal lines, which go up and down (North and South) the Y axis.
Its easy to think that since they are horizontal lines, they would be on the x axis, but they are not.
So similarly, the X axis is Longitude, as the values shift left to right (East and West) along the X axis.
Confusing for the same reason since on a north facing map, these lines are vertical.

## DMS vs DD

The degrees, minutes, seconds (DMS) coordinate values need to be convert to decimal degrees (dd) before calculation.

- http://www.rapidtables.com/convert/number/degrees-to-degrees-minutes-seconds.htm
- http://www.rapidtables.com/convert/number/degrees-minutes-seconds-to-degrees.htm

### How to convert decimal degrees to degrees,minutes,seconds

One degree (°) is equal to 60 minutes (') and equal to 3600 seconds ("):
    1° = 60' = 3600"

The integer degrees (d) are equal to the integer part of the decimal degrees (dd):
    d = integer(dd)

The minutes (m) are equal to the integer part of the decimal degrees (dd) minus integer degrees (d) times 60:
    m = integer((dd - d) × 60)

The seconds (s) are equal to the decimal degrees (dd) minus integer degrees (d) minus minutes (m) divided by 60 times 3600:
    s = (dd - d - m/60) × 3600

Example:

Convert 30.263888889° angle to degrees,minutes,seconds:
    d = integer(30.263888889°) = 30°
    m = integer((dd - d) × 60) = 15'
    s = (dd - d - m/60) × 3600 = 50"

Result:
    30.263888889° = 30° 15' 50"

## Decimal Degrees & Accuracy


### Degree precision versus length

| decimal places	| decimal degrees	| DMS	| qualitative scale that can be identified	| N/S or E/W at equator	| E/W at 23N/S	| E/W at 45N/S	| E/W at 67N/S |
|---|---|---|---|---|---|---|---|
| 0	| 1.0	| 1° 00′ 0″	| country or large region	| 111.32 km	| 102.47 km	| 78.71 km	| 43.496 km |
| 1	| 0.1	| 0° 06′ 0″	| large city or district	| 11.132 km	| 10.247 km	| 7.871 km	| 4.3496 km |
| 2	| 0.01	| 0° 00′ 36″	| town or village	| 1.1132 km	| 1.0247 km	| 787.1 m	| 434.96 m |
| 3	| 0.001	| 0° 00′ 3.6″	| neighborhood, street	| 111.32 m	| 102.47 m	| 78.71 m	| 43.496 m |
| 4	| 0.0001	| 0° 00′ 0.36″	| individual street, land parcel	| 11.132 m	| 10.247 m	| 7.871 m	| 4.3496 m |
| 5	| 0.00001	| 0° 00′ 0.036″	| individual trees	| 1.1132 m	| 1.0247 m	| 787.1 mm	| 434.96 mm |
| 6	| 0.000001	| 0° 00′ 0.0036″	| individual humans	| 111.32 mm	| 102.47 mm	| 78.71 mm	| 43.496 mm |
| 7	| 0.0000001	| 0° 00′ 0.00036″	| practical limit of commercial surveying	| 11.132 mm	| 10.247 mm	| 7.871 mm	| 4.3496 mm |
| 8	| 0.00000001	| 0° 00′ 0.000036″	| specialized surveying (e.g. tectonic plate mapping)	| 1.1132 mm	| 1.0247 mm	| 787.1 µm	| 434.96 µm |

- A value in decimal degrees to a precision of 4 decimal places is precise to 11.132 meters at the equator.
- A value in decimal degrees to 5 decimal places is precise to 1.1132 meter at the equator.
- Elevation also introduces a small error. At 6,378 m elevation, the radius and surface distance is increased by 0.001 or 0.1%.
- Because the earth is not flat, the precision of the longitude part of the coordinates increases the further from the equator you get.
- The precision of the latitude part does not increase so much, more strictly however, a meridian arc length per 1 second depends on latitude at point concerned.
- The discrepancy of 1 second meridian arc length between equator and pole is about 0.3 metres because the earth is an oblate spheroid.
