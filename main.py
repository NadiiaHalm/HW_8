from datetime import date, datetime, timedelta
from collections import defaultdict


def get_birthdays_per_week(users):
    celebrate_dict = defaultdict(list)
    today = date.today()
    next_week = timedelta(days=7)
    if not users:
        return {}
    for user in users:
        name = user['name']
        birthday = user['birthday']
        if birthday.month == 1:
            birthday_in_year = birthday.replace(year=today.year + 1)
        else:
            birthday_in_year = birthday.replace(year=today.year)
        day_of_week = birthday_in_year.isoweekday()
        if today < birthday_in_year < today + next_week:
            if day_of_week == 6 or day_of_week == 7:
                celebrate_dict['Monday'].append(name)
            else:
                celebrate_dict[birthday_in_year.strftime('%A')].append(name)

    return celebrate_dict


if __name__ == "main":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
