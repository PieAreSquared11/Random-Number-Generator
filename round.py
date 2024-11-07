import math

def round_to_place_value(value, p_val=0, highest=False):
    if not highest:
        if type(math.log(p_val)) != "float":
            value /= p_val

            value = round(value)

            value *= p_val
        
            return value
        else:
            print("unexpected value")
            raise ValueError
    else:
        str_val = str(value)

        if "." in str_val:
            p_val = 10 ** (len(str_val.split(".")[0]) - 1)

            return round_to_place_value(value, p_val=p_val)
        else:
            p_val = 10 ** (len(str_val) - 1)

            return round_to_place_value(value, p_val=p_val)
        

# EXAMPLE: print(round_to_place_value(2297.65, highest=True))