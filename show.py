"""
This module have functions
for show the calendar.
"""

from turtle import pos
from rich.table import Table
from rich.text import Text
from models.mycalendar import MyCalendar
from helpers.utils import console
from data.months import MONTHS


def change_days_year(data: list):
    """
    Validate the days
    for change 0 to '--' in case the day
    is of other month.
    """

    for month in data:
        for week in month:
            for days in week:
                for idx, day in enumerate(days):
                    if day == 0:
                        days[idx] = "--"

    return data


def change_days_month(data: list):
    """
    Validate the days
    for change 0 to '--' in case the day
    is of other month. But only for a month
    """

    for days in data:
        for idx, day in enumerate(days):
            if day == 0:
                days[idx] = "--"

    return data


def show_table(table: Table) -> None:
    """
    Show the table passed for paremeter
    """

    console.print(table)
    print("\n")


def select_data(calendar: MyCalendar) -> tuple:
    """
    Return a tuple
    with the data selected to use
    of calendar passed for parameter.
    """
    # getting data of calendar passed
    year = calendar.year
    month = calendar.month
    data = calendar.days

    return year, month, data


def create_month_message(month: str) -> str:
    """
    Return the message for show
    as header in each month.
    """

    message = Text(month)
    message.stylize("blue underline")

    return message


def get_name_month(month_number: str) -> str:
    """
    Validate the number of month passed
    for parameter for return your name.
    """

    return MONTHS[int(month_number) - 1]


def show_calendar(calendar: MyCalendar):
    """
    Show the calendar in a table
    """

    year, month, data = select_data(calendar)

    if month == "all":
        console.print(f"\nCalendar [bold underline]{year}[/bold underline]")
        console.print(month)
        for idx, month in enumerate(data):
            message = create_month_message(MONTHS[idx])

            # creating table for each month and columns
            table = Table(title=message, style="blue")
            table.add_column("Monday", justify="center")
            table.add_column("Tuesday", justify="center")
            table.add_column("Wednesday", justify="center")
            table.add_column("Thursday", justify="center")
            table.add_column("Friday", justify="center")
            table.add_column("Saturday", justify="center", style="green")
            table.add_column("Sunday", justify="center", style="green")

            days = change_days_year(data)
            for week in month:
                for days in week:
                    # for each day a row
                    table.add_row(
                        str(days[0]),
                        str(days[1]),
                        str(days[2]),
                        str(days[3]),
                        str(days[4]),
                        str(days[5]),
                        str(days[6]),
                    )
            # showing table
            show_table(table)

    else:
        month_name = get_name_month(month)

        console.print(
            f"\nCalendar [bold underline]{month_name}[/bold underline] [bold underline]{year}[/bold underline]"
        )

        month_name = create_month_message(month_name)

        # # creating table for each month and columns
        table = Table(title=month_name, style="blue")
        table.add_column("Monday", justify="center")
        table.add_column("Tuesday", justify="center")
        table.add_column("Wednesday", justify="center")
        table.add_column("Thursday", justify="center")
        table.add_column("Friday", justify="center")
        table.add_column("Saturday", justify="center", style="green")
        table.add_column("Sunday", justify="center", style="green")

        data = change_days_month(data)
        for week in data:
            # for each day a row
            table.add_row(
                str(week[0]),
                str(week[1]),
                str(week[2]),
                str(week[3]),
                str(week[4]),
                str(week[5]),
                str(week[6]),
            )
        # showing table
        show_table(table)
