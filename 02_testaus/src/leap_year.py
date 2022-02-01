
def is_leap_year(year: int) -> bool:
    '''
    Extra days occur in each year which is an integer multiple of 4 
    (except for years evenly divisible by 100, but not by 400).
    https://en.wikipedia.org/wiki/Leap_year
    '''

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
