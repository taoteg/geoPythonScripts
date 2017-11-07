
"""
# Convert DMS to DD.
def dd2dms_old(longitude, latitude):
    # math.modf() splits whole number and decimal into tuple
    # eg 53.3478 becomes (0.3478, 53)
    split_degx = math.modf(longitude)

    # the whole number [index 1] is the degrees
    degrees_x = int(split_degx[1])

    # multiply the decimal part by 60: 0.3478 * 60 = 20.868
    # split the whole number part of the total as the minutes: 20
    # abs() absoulte value - no negative
    minutes_x = abs(int(math.modf(split_degx[0] * 60)[1]))

    # multiply the decimal part of the split above by 60 to get the seconds
    # 0.868 x 60 = 52.08, round excess decimal places to 2 places
    # abs() absoulte value - no negative
    seconds_x = abs(round(math.modf(split_degx[0] * 60)[0] * 60, 2))

    # repeat for latitude
    split_degy = math.modf(latitude)
    degrees_y = int(split_degy[1])
    minutes_y = abs(int(math.modf(split_degy[0] * 60)[1]))
    seconds_y = abs(round(math.modf(split_degy[0] * 60)[0] * 60, 2))

    # account for E/W & N/S
    if degrees_x < 0:
        EorW = "W"
    else:
        EorW = "E"

    if degrees_y < 0:
        NorS = "S"
    else:
        NorS = "N"

    # abs() remove negative from degrees, was only needed for if-else above
    print("\t" + str(abs(degrees_x)) + u"\u00b0 " + str(minutes_x) + "' " + str(seconds_x) + "\" " + EorW)
    print("\t" + str(abs(degrees_y)) + u"\u00b0 " + str(minutes_y) + "' " + str(seconds_y) + "\" " + NorS)
"""


########################
# Module Method Testing.
########################


"""
# Test dd2dms()

coords = [["Dublin", -6.2597, 53.3478],["Paris", 2.3508, 48.8567],["Sydney", 151.2094, -33.8650],["Ft.Worth", -97.546649, 32.550058],["Dallas", -97.034774, 32.987978]]

for city,x,y in coords:
    print(city + ":")
    dd2dms(x, y)

# Expected Results:
# Dublin:       6° 15' 34.92" W, 	53° 20' 52.08" N
# Paris: 	    2° 21' 2.88" E, 	48° 51' 24.12" N
# Sydney:       151° 12' 33.84" E,  33° 51' 54.0" S
# Ft.Worth:     97° 32' 47.94" W,   32° 33' 0.21" N
# Dallas:       97° 2' 5.19" W,     32° 59' 16.72" N

# latDD(!Latitude!)
test_latDD = latDD('6° 15' 34.92"')
print(test_latDD)
"""

# INPUTS TESTS.
# Coordinate A DD:      32.550058,-97.546649
# Coordinate A DMS:     32°33'00.2"N 97°32'47.9"W
# Coordinate B DD:      32.987978,-97.034774
# Coordinate B DMS:     32°59'16.7"N 97°02'05.2"W

# print("------------------------------")
# print("""Inputs: 32°33'00.2"N 97°32'47.9"W | 32.550058,-97.546649""")
# # CORRECT SOLUTION! Comma between coords, added comma to split list in method.
# dd = parse_dms("""32°33'00.2"N, 97°32'47.9"W""")
# print(dd)
# print(dd2dms(32.550058))
# print(dd2dms(-97.546649))
# print("\n")
#
# print("------------------------------")
# print("""Inputs: 32°59'16.7"N 97°02'05.2"W | 32.987978,-97.034774""")
# # CORRECT SOLUTION! Comma between coords, added comma to split list in method.
# dd = parse_dms("""32°59'16.7"N, 97°02'05.2"W""")
# print(dd)
# print(dd2dms(32.987978))
# print(dd2dms(-97.034774))
# print("\n")
