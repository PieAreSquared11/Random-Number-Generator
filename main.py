from datetime import datetime
import round

def set_p_value(value, p_val):
    str_val = str(value)

    if "." in str_val:
        p_val = 10 ** len(str_val.split(".")[0])

        return value / p_val
    else:
        p_val = 10 ** len(str_val)

        return value / p_val

def rand():
    date = datetime.now()

    result = abs(date.year - date.month - date.day + date.hour - date.minute + date.second + date.microsecond)

    result = round.round_to_place_value(result, highest=True)

    result = set_p_value(result, 0.1)

    return result