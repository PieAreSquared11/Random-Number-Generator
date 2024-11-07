from datetime import datetime

date = datetime.now()

result = date.year + date.month + date.day + date.hour + date.minute + date.second + date.microsecond

print(result)