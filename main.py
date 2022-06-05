import csv
import requests
from alpha_vantage.timeseries import TimeSeries

API_key = 'NNJ0QXGXAFBPOTIF'

# ts = TimeSeries(API_key, output_format='pandas')
# data = ts.get_monthly_adjusted('SPY')

CSV_URL = (
    f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY_EXTENDED&symbol=SPY&interval=15min&slice=year1month1&apikey={API_key}")

dict_1 = {}

with requests.Session() as s:
    download = s.get(CSV_URL)
    decoded_content = download.content.decode('utf-8')
    cr = csv.DictReader(decoded_content.splitlines(), delimiter=',')
    # for row in cr:
    #   print(row)


def print_time(result: csv.DictReader) -> None:
    prev = '2022-06-03'
    price = 0
    for row in result:
        time = row["time"].split(" ")
        date = time[0]
        clock = time[1]

        print(row)

        #if prev != date:
         #   prev = date
          #  print(date)


print_time(cr)
