from datetime import datetime, timedelta

now = datetime.now()
print("Current date and time:", now)

formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted:", formatted)

birthday = datetime(2005, 1, 20)
print("My birthday:", birthday.date())

age_days = (now - birthday).days
print("Days since my birthday:", age_days)

next_week = now + timedelta(days=7)
print("One week from now:", next_week.date())
