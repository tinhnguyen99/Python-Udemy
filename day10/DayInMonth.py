# Author: Tinh Nguyen <tinh.nguyentrung1999@gmail.com>
# 100 day with python
# day 10


def IsLeapYear(Year):
    if Year % 4 == 0:
        #do something
        if Year % 100 == 0:
            #do something
            if Year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(Year, Month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    Day_return = month_days[Month - 1]
    if IsLeapYear(Year) and Month == 2:
        Day_return += 1
    return Day_return



#🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
