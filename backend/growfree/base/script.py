from . import models 


from itertools import combinations
from collections import defaultdict

def create_user_pairs():
    # Retrieve all Research_help instances from the database

    all_helpers = models.Research_help.objects.all()

    # Create a dictionary to store users based on interests
    interest_users = defaultdict(list)
    for helper in all_helpers:
        for interest in helper.interests.all():
            interest_users[interest].append(helper)

    # Create pairs of users with common interests
    user_pairs = []
    for interest, users in interest_users.items():
        if len(users) >= 2:
            pairs = list(combinations(users, 2))
            user_pairs.extend(pairs)

    return user_pairs

print(create_user_pairs()) 
