import math

def round_to_place_value(value, p_val):
    if type(math.log(p_val)) != "float":
        value /= p_val

        value = round(value)

        value *= p_val
    
        return value
    else:
        print("unexpected value")
        raise ValueError
        

print(round_to_place_value(2297, 100))