from datetime import *
from time import *
d1=date(2026,5,24)
d2=date(2026,5,28)
diff=d2-d1
#### time delta use ####

#weeks days hours minutes seconds milliseconds microseconds
# Create a base date
today = date(2026,6,5)

# Define a 7-day duration
one_week = timedelta(days=60)

# Calculate a future date
next_week = today + one_week
print(next_week)

print(diff)
# while True:
#     x=datetime.now()
#     print(x.time())
#     print(x.strftime("%H:%M:%S"))
#     sleep(1)