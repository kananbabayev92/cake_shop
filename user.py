from random import randrange
import random

USERS = [
    {
        "name": "Leyla",
        "user_wallet": randrange(100, 1000, 50),
        "cost":0,
        "basket":0
    },
    {
        "name": "Kanan",
        "user_wallet": randrange(100, 1000, 50),
        "cost":0,
        "basket":0
    },
    {
        "name": "John",
        "user_wallet": randrange(100, 1000, 50),
        "cost":0,
        "basket":0
    }
]


user_names = [user["name"] for user in USERS]

random_user = random.choice(user_names)
print(random_user)




