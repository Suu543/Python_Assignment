import sys


class Time:

    def __init__(self, hr, mn, sec):
        self.hr = hr
        self.mn = mn
        self.sec = sec

    def __str__(self):
        return f'({int(self.hr):2}:{int(self.mn):2}:{int(self.sec):2})'

    def getHour(self):
        return self.__hr

    def getMinute(self):
        return self.__mn

    def getSecond(self):
        return self.__sec

    def setHour(self, h):
        try:
            hour = int(h)
            if hour < 0 or hour > 24:
                raise Exception("Invalid Hour")
        except Exception as err:
            print("Invalid Hour")
            sys.exit(err)
        else:
            self.__hr = hour

    def setMinute(self, m):
        try:
            minute = int(m)
            if minute < 0 or minute > 24:
                raise Exception("Invalid Minute")
        except Exception as err:
            print("Invalid Minute")
            sys.exit(err)
        else:
            self.__mn = minute

    def setSecond(self, s):
        try:
            second = int(s)
            if second < 0 or second > 24:
                raise Exception("Invalid Second")
        except Exception as err:
            print("Invalid Second")
            sys.exit(err)
        else:
            self.__sec = second


if __name__ == "__main__":
    times = [
        Time(23, 59, 59),
        Time(9, 0, 5),
        Time(13, 30, 0),
        Time(3, 59, 59),
        Time(0, 0, 0),
        Time(1, 1, 1)
    ]

    print("times before sorting : ")
    for t in times:
        print(t)

    sortedTimes = sorted(times, key=lambda x: (x.hr, x.mn, x.sec))

    print("\ntimes after sorting : ")
    for t in sortedTimes:
        print(t)
