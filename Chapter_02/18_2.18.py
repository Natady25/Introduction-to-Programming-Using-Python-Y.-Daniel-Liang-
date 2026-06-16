import time

time_zone_offset = int(input("Enter the time zone offset to GMT: "))

current_time = time.time()

total_seconds = int(current_time)
current_second = total_seconds % 60

total_minutes = total_seconds // 60
current_minute = total_minutes % 60

total_hours = total_minutes // 60
current_hour_gmt = total_hours % 24

current_hour = (current_hour_gmt + time_zone_offset) % 24

print(f"The current time is {current_hour:02d}:{current_minute:02d}:{current_second:02d}")