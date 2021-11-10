# in this programme we learn how to know the the leapyear
year = int(input("Enter a year to check leap year or not :"))
if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print("{0} is a leap year ".format(year))
        else:
            print("{0} is not a leap year ".format(year))
    else:
        print("{0} is a leap year ".format(year))
else:
    print("{0} is not a leap year ".format(year))

