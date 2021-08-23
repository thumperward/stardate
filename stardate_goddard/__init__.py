# Calculations taken from stardate script by Phillip L. Sublett
# <TrekMaster@TrekGuide.com>
# http://trekguide.com/Stardates.htm#TNG

import math
from dateutil.parser import parse
from datetime import datetime
import argparse
import time


def get_stardate(date, verbose=False):
    requested_date = parse(date)
    origin_date = parse("2318-07-05T12:00:00-00:00")

    if verbose:
        print(f'Start date: {requested_date.strftime("%Y-%m-%d %H:%M:%S")}')
        print(f'Origin date: {origin_date.strftime("%Y-%m-%d %H:%M:%S")}')
    begin = time.mktime(requested_date.timetuple())*1000
    end = time.mktime(origin_date.timetuple())*1000
    stardate = begin - end
    if verbose:
        print(f"Selection date - origin date = {str(stardate)}")
    stardate = stardate / 34367056.4
    stardate = math.floor(stardate * 10) / 10
    if verbose:
        print(f"Previous value / 34367056.4 and floored = {str(stardate)}")
    return stardate


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-v",
        "--verbose",
        help="See more variables and the calculation process",
        action="store_true",
    )
    parser.add_argument(
        "-d",
        "--date",
        help="The date to convert to stardate, format YYYY-MM-DD",
        metavar="D",
        type=str,
        required=True,
    )
    args = parser.parse_args()

    print(get_stardate(args.date, args.verbose))
