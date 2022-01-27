""""
This module have the
functions for work
with the arguments passed in the execution.
"""

from optparse import OptionParser
from messages.help import YEAR_MESSAGE, MONTH_MESSAGE
from datetime import datetime
from messages.help import USAGE

# functions of config
get_date_current = lambda: {"year": str(datetime.now().year), "month": str(datetime.now().month)}


def get_options() -> tuple:
    """
    Return a tuple with the options
    and arguments passed for parameter.
    """

    parser = OptionParser(usage = USAGE)

    parser.add_option(
        "-y",
        "--year",
        dest="year",
        default=get_date_current()["year"],
        help=YEAR_MESSAGE,
    )

    parser.add_option(
        "-m",
        "--month",
        dest="month",
        default='all',
        help=MONTH_MESSAGE,
    )

    options, args = parser.parse_args()
    del args  # no use yet

    return options
