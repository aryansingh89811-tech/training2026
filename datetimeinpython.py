from datetime import *
print(datetime.now())

x=datetime.now()
print(x.date())
print(x.time())
print(x.strftime("%A"))
print(x.strftime("%a"))
print(x.strftime("%H"))
print(x.strftime("%M"))
print(x.strftime("%S"))