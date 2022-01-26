"""
This file have the data
about of the months.
"""

# list for set in each table
MONTHS = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

# list for validate the month for number
OPTIONS_MONTHS = ["all"]
# adding values
for i in range(12):
    OPTIONS_MONTHS.append(str(i + 1))
