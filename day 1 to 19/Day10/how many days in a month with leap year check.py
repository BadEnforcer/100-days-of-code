def is_leap(given_year):
    if given_year % 4 == 0:
        if given_year % 100 == 0:
            if given_year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(given_year, given_month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    leap = is_leap(given_year)
    if leap:
        month_days[1] = 29
    index = given_month - 1
    return month_days[index]


# 🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
is_leap(year)
days = days_in_month(year, month)
print(days)
