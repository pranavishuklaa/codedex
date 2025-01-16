#datetime

import datetime, bday_message 

today = datetime.date.today()
next_birthday = datetime.date(2004, 4, 9)
days_away = today - next_birthday

if next_birthday == today:
    print(bday_message.random_message)
else:
    print(f"My next birthday is in {days_away.days} days away!")