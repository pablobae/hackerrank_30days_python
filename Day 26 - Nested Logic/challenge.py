import datetime


def calculate_fine(expected_date: datetime, returned_date: datetime) -> int:
    day_multiplicator = 15
    month_multiplicator = 500
    year_multiplicator = 10000

    fine = 0
    if returned_date > expected_date and returned_date.month == expected_date.month and returned_date.year == expected_date.year:
        fine = (returned_date.day - expected_date.day) * day_multiplicator
    elif returned_date > expected_date and returned_date.month > expected_date.month and returned_date.year == expected_date.year:
        fine = (returned_date.month - expected_date.month) * month_multiplicator
    elif returned_date.year > expected_date.year:
        fine = year_multiplicator

    return fine


if __name__ == '__main__':
    returned_data = list(map(int, input().strip().split(' ')))
    expected_data = list(map(int, input().strip().split(' ')))

    returned_date = datetime.date(returned_data[2], returned_data[1], returned_data[0])
    expected_date = datetime.date(expected_data[2], expected_data[1], expected_data[0])

    print(calculate_fine(expected_date, returned_date))
