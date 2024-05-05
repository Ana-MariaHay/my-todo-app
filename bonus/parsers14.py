def parse(feet_inches):
    calc_list = feet_inches.split(" ")
    feet = float(calc_list[0])
    inches = float(calc_list[1])
    return {"feet": feet, "inches": inches}  # dictionary, can be accessed via the key
