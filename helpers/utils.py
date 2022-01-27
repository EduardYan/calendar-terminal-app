"""
Utils functions or data to use
"""

from rich.console import Console
from rich.text import Text
from rich.theme import Theme
from rich.panel import Panel
from rich import print
from config import NAME, VERSION
from messages import errors

# console for use to show messages
console = Console()
text = Text()

# testing
# theme for message
# message_theme = Theme(
#   {
#     'message': 'blue'
#   }
# )


def show_year_invalid() -> None:
  """
  Show the message when the year
  is invalid.
  """


  message = errors.YEAR_INVALID
  panel = Panel(
    f'[red]{message}[/red]\t\t\t\t\t\t\t\t\t[green]Version {VERSION}[/green]',
    title = NAME,
    border_style="blue"
  )
  print(panel)

def show_month_invalid() -> None:
  """
  Show the message when the month
  is invalid.
  """

  message = errors.MONTH_INVALID
  panel = Panel(
    f'[red]{message}[/red]\t\t\t\t\t\t\t\t\t[green]Version {VERSION}[/green]',
    title = NAME,
    border_style="blue"
  )
  print(panel)