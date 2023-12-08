import time

print(time.asctime()) # Thu Nov  2 06:27:45 2023

lt = time.localtime()
print(lt) # time.struct_time(tm_year=2023, tm_mon=11, tm_mday=2, tm_hour=6, tm_min=27, tm_sec=45, tm_wday=3, tm_yday=306, tm_isdst=0)
print(lt[0]) # 2023
print(lt.tm_year) # 2023
print(lt.tm_zone) # E. South America Standard Time
print(time.asctime(lt)) # Thu Nov  2 06:45:21 2023

lt2 = time.localtime(0) # Based on parameter time in seconds
print(lt2) # time.struct_time(tm_year=1969, tm_mon=12, tm_mday=31, tm_hour=21, tm_min=0, tm_sec=0, tm_wday=2, tm_yday=365, tm_isdst=0)
print(lt2[0]) # 1969
print(lt2.tm_year) # 1969
print(lt2.tm_zone) # E. South America Standard Time
print(time.asctime(lt2)) # Wed Dec 31 21:00:00 1969

print(time.time()) # 1698917543.6573582 # Time in seconds (float, tho)

time.sleep(0.2) # Makes the execution stops for this interval (seconds)

print(time.process_time()) # Time between another execution of the application
