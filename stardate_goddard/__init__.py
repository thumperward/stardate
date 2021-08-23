import math
from dateutil.parser import parse
from datetime import datetime
import argparse
import time


def get_stardate(date=None, verbose=False):
    # Calculations taken from stardate script by Phillip L. Sublett
    # <TrekMaster@TrekGuide.com>
    # http://trekguide.com/Stardates.htm#TNG
    requested_date = datetime.now() if date is None else parse(date)
    origin_date = parse("2318-07-05T00:00:00-00:00")

    if verbose:
        print(f"Start Date : " + requested_date.strftime("%Y-%m-%d %H:%M:%S"))
        print(f"Origin Date : " + origin_date.strftime("%Y-%m-%d %H:%M:%S"))
    stardate = time.mktime(requested_date.timetuple()) - time.mktime(
        origin_date.timetuple()
    )
    if verbose:
        print(f"Selection Date - Origin Date = {str(stardate)}")
    stardate = stardate / 34367.0564
    stardate = math.floor(stardate * 10) / 10
    if verbose:
        print(f"Previous Value / 34367056.4 and floored = {str(stardate)}")
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

    if args.verbose and args.date is None:
        print("Using current date")

    print(get_stardate(args.date, args.verbose))
