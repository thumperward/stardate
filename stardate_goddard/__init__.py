import math
from dateutil.parser import parse
from datetime import datetime
import argparse
import time


def get_stardate(date=None, verbose=False):
    requested_date = datetime.now() if date is None else parse(date)
    origin_date = parse("1987-07-15T00:00:00-00:00")

    if verbose:
        print(f"Start Date : " + requested_date.strftime("%Y-%m-%d %H:%M:%S"))
        print(f"Origin Date : " + origin_date.strftime("%Y-%m-%d %H:%M:%S"))
        print("---------------------")
        print(f'Year : {requested_date.strftime("%Y")}')
        print(f'Month : {requested_date.strftime("%m")}')
        print(f'Day : {requested_date.strftime("%d")}')
        print(f'Hour : {requested_date.strftime("%H")}')
        print(f'Minutes : {requested_date.strftime("%M")}')
        print(f'Seconds : {requested_date.strftime("%S")}')
        print("---------------------")

    stardate = time.mktime(requested_date.timetuple()) - time.mktime(
        origin_date.timetuple()
    )
    if verbose:
        print(f"Selection Date - Origin Date = {str(stardate)}")
        print("---------------------")

    stardate = stardate / (60.0 * 60.0 * 24.0 * 0.036525)
    if verbose:
        print(f"Previous Value / (60 * 60 * 24 * 0.036525) = {str(stardate)}")
        print("---------------------")
    stardate = math.floor(stardate + 410000.0)
    if verbose:
        print(f"Floor(Previous Value + 410000.0) = {str(stardate)}")
        print("---------------------")
    stardate = stardate / 10.0
    if verbose:
        print(f"Previous Value / 10.0 = {str(stardate)}")
        print("---------------------")

    if verbose:
        print("Stardate Final : " + str(stardate))
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
        default=None,
    )
    args = parser.parse_args()

    if args.verbose:
        print("---Initializing---")
        if args.date is None:
            print("Using current date")

    print(get_stardate(args.date, args.verbose))
