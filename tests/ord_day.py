import datetime


def day_of_year():
    year = input('输入year:')
    month = input('month:')
    day = input('day:')
    input_day = datetime.date(int(year), int(month), int(day))
    year_day = datetime.date(int(year), 1, 1)
    print((input_day - year_day).days + 1)


if __name__ == '__main__':
    day_of_year()
