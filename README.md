# Time Calculator

Overview

This Python project features a function `add_time` that takes a start time, a duration, and optionally a starting day, then calculates the resulting time and day. The project handles time in both 12-hour and 24-hour formats and accounts for day transitions.

Features

- Calculates the end time after adding a duration to a start time.
- Handles AM/PM distinction and transitions between days.
- Optional handling of days of the week.

Installation

This project requires no external libraries and runs with Python's standard libraries.

Usage

To use the `add_time` function, simply import it and provide the start time, duration, and optionally the starting day.

Example:
```python
from time_calculator import add_time

print(add_time("3:00 PM", "3:10"))

Testing

Test cases are provided to demonstrate the functionality, including handling of different time formats and day transitions.

Contributing

Contributions, bug reports, and feature requests are welcome. Please check the CONTRIBUTING.md file for guidelines on contributing.

License

This project is released under the MIT License. See the LICENSE file for more details.

