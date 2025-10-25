


reminder = []
while True:
    menu = input("Choose an option:\n1. Add Reminder\n2. View Reminders\n3. Exit\n> ")
    if menu == '1':
        reminder_text = input('Enter your reminder: ')
        reminder.append(reminder_text)
        print('Reminder added!')
    elif menu == '2':
        if len(reminder) != 0:
            for rem in reminder:
                print("Your reminders are ...")
                print(f'- {rem}')
            
        else:
            print('No reminders found.')
    elif menu == '3':
        print('Exiting the reminder app.')
        break
    