from datetime import datetime
import round

date = datetime.now()

result = date.year + date.month + date.day + date.hour + date.minute + date.second + date.microsecond

result = round.round_to_place_value(result, highest=True)

print(result)