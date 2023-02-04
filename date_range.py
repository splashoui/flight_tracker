from datetime import timedelta


def choose_date_range(start_date, end_date):
    """
    Get the list of date range.
    Parameters
        start_date: The start date.
        end_date: The end date.
    """

    date_range = [start_date + timedelta(days=x)
                  for x in range(0, (end_date-start_date).days+1)]

    return date_range
