def cars(manufacturer, model, **car_info):
    """
    :param manufacturer: str
    :param model: str
    :param car_info: dict key, value
    :return: dictionary of all the stored info about a car
    """
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info


car_profile = cars('subaru', 'outback', colour='blue', tow_package='true')
print(car_profile)