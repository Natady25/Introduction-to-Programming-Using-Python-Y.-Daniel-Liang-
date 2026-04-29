# Versi 1
distance_in_kilometers = 14
distance_in_miles = 14 * (1 / 1.6)
time_in_hours = 45.5 * (1 / 60)
print("Average Speed in Miles per Hour=", distance_in_miles / time_in_hours, "miles per hours")

# Versi 2
kilometers = 14
minutes = 45
seconds = 30

miles = kilometers / 1.6
total_hours = (minutes / 60) + (seconds / 3600)

average_speed = miles / total_hours

print("Average speed = ", average_speed, "miles per hours")
