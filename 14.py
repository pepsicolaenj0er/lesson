from datetime import datetime , timedelta

users = [
    {"name": "Alice", "last_login": "2025-08-01"},
    {"name": "Bob", "last_login": "2025-09-15"},
    {"name": "Charlie", "last_login": "2025-07-20"},
    {"name": "Diana", "last_login": "2025-09-10"},
]
today = datetime.today().date()
deactiveUsers = []
for user in users:
    last_login = datetime.strptime(user["last_login"], "%Y-%m-%d").date()
    if today - last_login > timedelta(days=30):
        deactiveUsers.append(user["name"])

print(deactiveUsers)
print(len(deactiveUsers))
            

