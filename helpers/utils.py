"""
Utils functions or data to use
"""

from rich.console import Console
from rich.text import Text
from rich.theme import Theme
from messages import errors

# console for use to show messages
console = Console()
text = Text()

# theme for message
message_theme = Theme(
  {
    'message': 'blue'
  }
)


def show_year_invalid() -> None:
  """
  Show the message when the year
  is invalid.
  """

  console = Console(theme = message_theme)

  message = Text(errors.YEAR_INVALID)
  message.stylize('bold red', 0 , 43)
  message.stylize('bold underline green', 44, 54)
  console.print('\n================== CALENDAR APP =====================', style = 'message')
  console.print(message)
  console.print('=====================================================\n', style = 'message')

def show_month_invalid() -> None:
  """
  Show the message when the month
  is invalid.
  """

  console = Console(theme = message_theme)

  message = Text(errors.MONTH_INVALID)
  message.stylize('bold red', 0 , 43)
  message.stylize('bold underline green', 45, 55)
  console.print('\n================== CALENDAR APP =====================', style = 'message')
  console.print(message)
  console.print('=====================================================\n', style = 'message')