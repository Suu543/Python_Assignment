import sys


class Date:
    def __init__(self, yr, mt, dy):
        self.yr = yr
        self.mt = mt
        self.dy = dy

    def __str__(self):
        return f'({self.yr}- {self.mt}-{self.dy})'

    def __lt__(self, other):
        return (self.yr, self.mt, self.dy) < (other.yr, other.mt, other.dy)

    def getYear(self):
        return self.__yr

    def getMonth(self):
        return self.__mt

    def getDay(self):
        return self.__dy

    def setYear(self, y):
        try:
            year = int(y)
            if year < 1:
                raise Exception("Invalid Year")
        except Exception as err:
            print("Invalid Year")
            sys.exit(err)
        else:
            self.__yr = year

    def setMonth(self, m):
        try:
            month = int(m)
            if month < 1 or month > 12:
                raise Exception("Invalid Month")
        except Exception as err:
            print("Invalid Month")
            sys.exit(err)
        else:
            self.__mt = month

    def setDay(self, d):
        try:
            day = int(d)
            if day < 1 or day > 31:
                raise Exception("Invalid Day")
        except Exception as err:
            print("Invalid Day")
            sys.exit(err)
        else:
            self.__dy = day


if __name__ == "__main__":
    dates = [
        Date(2020, 9, 24),
        Date(2000, 9, 15),
        Date(0, 2, 29),
        Date(1997, 2, 20),
        Date(2001, 5, 2),
        Date(2001, 5, 1),
        Date(1997, 3, 1),
    ]

    print("dates before sorting : ")
    for d in dates:
        print(d)

    sortedDates = sorted(dates, key=lambda x: (x.yr, x.mt, x.dy))

    print("\nstudents after sorting : ")
    for d in sortedDates:
        print(d)
