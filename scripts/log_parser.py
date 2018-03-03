import glob
from datetime import datetime

#import numpy as np
import pandas as pd

# 7.1.0.1.5 close dome
# 7.1.0.1.4 open dome


def main():

    dates = list()
    values = list()

    file_list = glob.glob("../data/telescope_log/*")
    for name in file_list:
        try:
            with open(name, 'r') as f:
                for line in f.readlines():
                    if  '[INFO ][2017/' in line and '7.1.0.1.4' in line and '<Open=true>' in line:
                        date = line[8:27].replace('/', '-')
                        dates.append(pd.Timestamp(date))
                        values.append(1.0)
                        print('OPEN: {}'.format(date))
                    elif '[INFO ][2017/' in line and '7.1.0.1.5' in line and '<Close=true>' in line:
                        date = line[8:27].replace('/', '-')
                        dates.append(pd.Timestamp(date))
                        values.append(0.0)
                        print('CLOSE: {}'.format(date))
        except UnicodeDecodeError:
            continue

    ts = pd.Series(values, dates)
    ts = ts.sort_index()
    ts.to_csv('../data/dome.csv')    
    print(ts.head(100))

if __name__=='__main__':
    main()