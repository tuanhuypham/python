def is_leap(year):
    if year <= 1900:
        return False
    else:
        year % 4 == 0
        return True
    return leap
year = int(input())
print(is_leap(year))

def is_leap(year):
    leap = False
    if year <= 1900:
        return False
    elif year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    return leap
year = int(input())
print(is_leap(year))
