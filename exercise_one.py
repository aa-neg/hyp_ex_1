months = {
    1: {
        "days": 31
    },
    2: {
        "days": 28
    },
    3: {
        "days": 31
    },
    4: {
        "days": 30
    },
    5: {
        "days": 31
    },
    6: {
        "days": 30
    },
    7: {
        "days": 31
    },
    8: {
        "days": 31
    },
    9: {
        "days": 30
    },
    10: {
        "days": 31
    },
    11: {
        "days": 30
    },
    12: {
        "days": 31
    },
}

def dateChecker(userDate):
    try:
        day = userDate.split('/')[0]
        month = userDate.split('/')[1]
        year = userDate.split('/')[2]

        if ((int(day) <= 0) or (int(month) <= 0) or (int(year) <= 0)):
            raise argparse.ArgumentTypeError("%s is an invalid positive value" % userDate)
        elif (len(day) != 2) or (len(month) != 2) or (len(year) != 4):
            raise argparse.ArgumentTypeError("%s is an invalid date. " % userDate)
        elif (int(year) < 1991) or (int(year) > 2999):
            raise argparse.ArgumentTypeError("%s is outside the available date range. " % userDate)

        return userDate

    except Exception as err:
        raise argparse.ArgumentTypeError("%s is an invalid date. " % userDate)

def isLeapYear(year):
    if (year % 4 != 0):
        return False
    elif (year % 100 != 0):
        return True
    elif (year % 400 != 0):
        return False
    else:
        return True

def calculateTotalDays(days, month, year):
    totalDays = 0

    totalDays += days

    for i in range(1, month + 1):
        totalDays += months[i]["days"]
        if (i == 2) and isLeapYear(year):
            totalDays += 1

    for i in range(1, year + 1):
        if isLeapYear(i):
            totalDays += 366
        else:
            totalDays += 365

    return totalDays

def daysBetweenDates(date1, date2):
    startDay = int(date1.split('/')[0])
    startMonth = int(date1.split('/')[1])
    startYear = int(date1.split('/')[2])


    endDay = int(date2.split('/')[0])
    endMonth = int(date2.split('/')[1])
    endYear = int(date2.split('/')[2])

    return abs(calculateTotalDays(startDay, startMonth, startYear) - calculateTotalDays(endDay, endMonth, endYear)) - 1


if __name__ == "__main__":
    import argparse

    argparser = argparse.ArgumentParser(
        usage="Find the total complete days between two dates"
        )

    argparser.add_argument(
        '--startDate', '-s'
        , type=dateChecker
        , help="Please enter a start date in form DD/MM/YYYY between 01/01/1901 and 31/12/2999 eg 30/01/2013 "
        )

    argparser.add_argument(
        '--endDate', '-e'
        , type=dateChecker
        , help="Please enter an end date in form DD/MM/YYYY between 01/01/1901 and 31/12/2999 eg 30/01/2013 "
        )

    arguments = argparser.parse_args()

    print("Number of full days elapsed: %s" % daysBetweenDates(arguments.startDate, arguments.endDate))

