# import sys
# import os
import glob


def main():
    file_list = glob.glob("../data/telescope_log/*")
    for name in file_list:
        try:
            with open(name, 'r') as f:
                for line in f.readlines():
                    if '7.1.0.1.4' in line and '[2017' in line:
                        print(line)
        except UnicodeDecodeError:
            continue

if __name__=='__main__':
    main()