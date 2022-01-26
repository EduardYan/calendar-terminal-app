"""
Model custom for a calendar
"""


class MyCalendar:
    """
    Model
    """

    def __init__(self, year: str, month: str, days: list) -> None:
        # values
        self.year = year
        self.month = month
        self.days = days
