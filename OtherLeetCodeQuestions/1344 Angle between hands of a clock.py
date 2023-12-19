


def angleClock(hour: int, minutes: int) -> float:

    hour = hour % 12
    hour_angle_from_12 = ((hour * 30) + (minutes * 0.5))
    minute_angle_from_12 = (minutes * 6) % 360
    result = abs(hour_angle_from_12 - minute_angle_from_12)
    return min(360 - result, result)


# Python program to find angle
# between hour and minute hands

# Function to Calculate angle b/w
# hour hand and minute hand
def calcAngle(h, m):
    # validate the input
    if (h < 0 or m < 0 or h > 12 or m > 60):
        print('Wrong input')

    if (h == 12):
        h = 0
    if (m == 60):
        m = 0
        h += 1;
        if (h > 12):
            h = h - 12;

    # Calculate the angles moved by
    # hour and minute hands with
    # reference to 12:00
    hour_angle = 0.5 * (h * 60 + m)
    print(hour_angle)
    minute_angle = 6 * m

    # Find the difference between two angles
    angle = abs(hour_angle - minute_angle)

    # Return the smaller angle of two
    # possible angles
    angle = min(360 - angle, angle)

    return angle


# Driver Code
h = 12
m = 30
print('Angle ', calcAngle(h, m))

# This code is contributed by Danish Raza


print(angleClock(12, 30)) #expected anwer : 165.0000












