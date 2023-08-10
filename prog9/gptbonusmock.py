import datetime as dt
import calendar

def getday():
    # Get the current date
    current_date = dt.datetime.now()

    # Get the day of the week as an integer (0 = Monday, 1 = Tuesday, ..., 6 = Sunday)
    day_of_week = current_date.weekday()

    # Make list of days
    days = list(calendar.day_name)

    # Find day based on index
    day = days[day_of_week]

    return day

def test_getday(monkeypatch):

    class MockDatetime(dt.datetime):
        @classmethod
        def now(cls):
            # Set the desired test date (2023, 8, 9 corresponds to Wednesday)
            return cls(2023, 8, 10)  # Replace with your desired test date

    monkeypatch.setattr(dt, "datetime", MockDatetime)

    x = getday()
    assert x == "Thursday"

