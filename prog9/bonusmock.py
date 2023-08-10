import datetime as dt
import calendar

def getday():
    # Get the current date
    current_date = dt.datetime.now()

    # Get the day of the week as an integer (0 = Monday, 1 = Tuesday, ..., 6 = Sunday)
    day_of_week = current_date.weekday()

    # make list of days
    days = list(calendar.day_name)

    #find day based on index
    day = days[day_of_week]

    return day

def test_getday(monkeypatch):

    def mockreturn():
        return "Thursday"

    monkeypatch.setattr(dt, "datetime", mockreturn())

    x = getday()
    assert x == "Thursday"





