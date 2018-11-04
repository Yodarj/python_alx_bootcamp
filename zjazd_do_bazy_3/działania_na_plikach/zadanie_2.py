import sys

# try:
#     sys.argv[1]
# except:
#     print("Podaj plik, ziomek")
#     quit()
#
# nazwa = sys.argv[1]
nazwa = 'logs.txt'

user_last_login = {}
user_total_time = {}

with open(f"dane/{nazwa}", encoding='utf-8') as f:
    for line in f:
        user, action, time = line.split(';')
        time = int(time)
        if action == 'LOGIN':
            user_last_login[user] = time
        if action == 'LOGOUT':
            user_total_time[user] = user_total_time.get(user, 0) + time-user_last_login[user]


print('''Czas przebywania w systemie:''')

for user in sorted(user_total_time.items(), key=lambda x: x[1], reverse = True):
    print(f'''- {user[0]}: {user[1]} sekund''')