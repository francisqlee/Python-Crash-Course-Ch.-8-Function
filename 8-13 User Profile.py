def build_profile(first, last, **user_info):
    """
    :param first: str
    :param last: str
    :param user_info: dictionary key, value
    :return: a dictionary containing everything we know about a user
    """
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile('francis', 'lee', education='bachelors',
                             university='ubc', year='4')

print(user_profile)