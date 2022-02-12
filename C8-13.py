def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['last_name'] = last
    user_info['first_name'] = first
    return user_info


user_profile = build_profile('Akshat', 'Agarwal',
                             age='16',
                             field='School',
                             location='Hong Kong')
print(user_profile)