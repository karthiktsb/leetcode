from datetime import datetime
from datetime import timedelta
import pytz

if __name__ == '__main__':
    date = datetime.strptime("2022-11-30", "%Y-%m-%d")

    print(date)
    print(datetime.now())
    print(datetime.strftime(datetime.now(), "%Y-%m-%d-%H:%M:%S"))

    date1 = datetime(2023, 10, 31)
    date2 = datetime(2023, 10, 15)

    diff = date1 - date2
    print(diff.days)

    date3 = datetime(2023, 4, 26)
    days = timedelta(days=5)

    print(date3 + days)


    timezone = pytz.timezone("US/Eastern")

    localized_time = timezone.localize(datetime.now())

    utc_time = localized_time.astimezone(pytz.timezone("Asia/Colombo"))
    print("Localized Time:", localized_time)
    print("UTC Time:", utc_time)

    print(pytz.all_timezones)