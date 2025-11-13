import time
from datetime import datetime

print("🕒 Reminder App 🕒")
reminder_msg = input("Enter your reminder (e.g., Meeting at 4 PM): ")
reminder_time = input("Enter time for reminder (HH:MM 24-hour format): ")

# Convert to datetime object for today
now = datetime.now()
reminder_hour, reminder_minute = map(int, reminder_time.split(":"))
reminder_datetime = now.replace(hour=reminder_hour, minute=reminder_minute, second=0, microsecond=0)

# If reminder time already passed today, set it for tomorrow
if reminder_datetime < now:
    reminder_datetime = reminder_datetime.replace(day=now.day + 1)

print(f"✅ Reminder set for {reminder_datetime.strftime('%H:%M')}")

# Wait until time
while True:
    current_time = datetime.now()
    if current_time >= reminder_datetime:
        print(f"\n🔔 Reminder: {reminder_msg} 🔔")
        break
    time.sleep(30)  # Check every 30 seconds

