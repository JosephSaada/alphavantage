import csv
import requests
from alpha_vantage.timeseries import TimeSeries

API_key = 'NNJ0QXGXAFBPOTIF'

# ts = TimeSeries(API_key, output_format='pandas')
# data = ts.get_monthly_adjusted('SPY')

CSV_URL = (
    f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY_EXTENDED&symbol=SPY&interval=15min&slice=year1month1&apikey={API_key}")

with requests.Session() as s:
    download = s.get(CSV_URL)
    decoded_content = download.content.decode('utf-8')
    cr = csv.DictReader(decoded_content.splitlines(), delimiter=',')
    # for row in cr:
    #   print(row)


class Data:
    pass


def print_time(result: csv.DictReader) -> None:
    result_list = list(cr)
    for row in reversed(result_list):
        time = row["time"].split(" ")
        date = time[0]
        clock = time[1]

        if clock == '09:30:00' or clock == '16:00:00':
            if clock == '09:30:00':
                open = row["open"]
                print(f"{date} {clock} {open} ", end='')
            if clock == '16:00:00':
                close = row["close"]
                print(f"{date} {clock} {close} ", end='')
                try:
                    dif = (float(close) - float(open))
                    diff = lambda x: True if x > 0 else False
                    print(f'{diff(dif)} ')
                except UnboundLocalError:
                    print()

        # if prev != date:
        #   prev = date
        #  print(date)
        # print(clock)


print_time(cr)
