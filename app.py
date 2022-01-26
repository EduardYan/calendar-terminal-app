#!/usr/bin/python3
"""
This is a terminal
applicattion for watch the calendars
of years and months.

Use Example:
-y The year
-m The month

------------------------
python3 app.py -y 2020 -m 12
python3 app.py --y 2020 -m 1
python3 app.py -m 5
------------------------

For see alls the options:
python3 app.py --help

"""

from calendar import Calendar, IllegalMonthError
from args import get_options
from helpers.utils import show_year_invalid, show_month_invalid
from show import show_calendar
from models.mycalendar import MyCalendar
from data.months import OPTIONS_MONTHS


def get_months_year(year: int, month="all") -> None:
    """
    Return a object of calendar
    with the days of the months
    and year passed for parameter
    to use.
    """

    calendar = Calendar()

    # validating for show alls the months or only one
    if month != "all":
        all_calendar = calendar.monthdayscalendar(int(year), int(month))
        return all_calendar
    else:
        all_calendar = calendar.yeardayscalendar(int(year), width=1)

        return all_calendar


if __name__ == "__main__":
    # getting the options
    options = get_options()
    year = options.year
    month = options.month

    # validating the data passed
    if year.isdigit():
        if month.isdigit() or month in OPTIONS_MONTHS:
            if month == "all":
                days = get_months_year(year)
                calendar = MyCalendar(year, month, days)

                show_calendar(calendar)

            else:
                try:
                    days = get_months_year(year, month)
                    calendar = MyCalendar(year, month, days)

                    show_calendar(calendar)
                # in case the ilegal number for the month
                except IllegalMonthError:
                    show_month_invalid()
        else:
            show_month_invalid()
    else:
        show_year_invalid()
