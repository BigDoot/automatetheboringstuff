#!python3

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    daysbtwyears = (year2 - year1)*365
    leapdays = 0
    
    for year in range(year1, year2 + 1):
        if year%4 == 0:
            leapdays += 1
            if year in [1900, 1800, 1700]:
                leapdays -= 1
    if year1%4 == 0  and month1 > 2:
        leapdays -= 1
    if year2%4 == 0 and month2 < 3:
        leapdays -= 1

    monthtodays = [0, 0 , 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    month1 = monthtodays[month1]
    month2 = monthtodays[month2]
    total = leapdays + daysbtwyears + (month2 - month1) + (day2 - day1)
    return total

def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        print(result, answer)
        if result != answer:
            print("Test with data:", args, "failed")
        else:
            print("Test case passed!")
test()
