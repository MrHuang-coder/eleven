def city_country(city, country, population=''):
    city_info = city + ', ' + country
    if population:
        city_info += ' - population ' + population
    return city_info

