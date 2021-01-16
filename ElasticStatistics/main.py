import pandas as pd
import datetime

if __name__ == '__main__':
    data_raw = []
    for mounth in range(12, 13):
        for day in range(15, 30):
            date=datetime.date(2020, mounth, day)
            print(date)
            data_raw.append([date,
                            2,
                            3])
    print(data_raw)

