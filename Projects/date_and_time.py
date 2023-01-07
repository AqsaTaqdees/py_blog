# Shows the current date and time
from datetime import datetime
currentDateAndTime = datetime.now()

print("The current date and time is", currentDateAndTime)

currentTime = currentDateAndTime.strftime("%H:%M:%S")
print("The current time is", currentTime)
